import pygame
import random

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ābolu rījējs')


class Snake:
    """klase Čūska apraksta čūskas, kā tās izskatās
    un darbojas"""
    
    def __init__(self, x, y):
        """init metodē apraksta objekta īpašības jeb atribūtus"""
        self.length = 1
        self.x_change = 0
        self.y_change = 0
        self.rectangles = [pygame.Rect(x, y, 20, 20)]

    def move(self):
        x = self.rectangles[-1].left
        y = self.rectangles[-1].top
        
        self.rectangles.append(
            pygame.Rect(x + self.x_change, y + self.y_change,
                        20, 20)
        )
        if len(self.rectangles) > self.length:
            self.rectangles.pop(0) 
    
    def is_out_of_bounds(self, window):
        window_rect = window.get_rect()
        return not window_rect.contains(self.rectangles[-1])

    def draw(self, window):
        pygame.draw.rect(window, [0, 125, 0], self.rectangles[-1])
    
        for rectangle in self.rectangles[:-1]:
            pygame.draw.rect(window, [13, 55, 13], rectangle)
            
            
class Apple:
    
    size = 15
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def is_eaten(self, snake):
        apple_rect = pygame.Rect(
            self.x, self.y,
            Apple.size, Apple.size
        )
        
        return apple_rect.colliderect(snake.rectangles[-1])
    
    def draw(self, window):
        apple_rect = pygame.Rect(
            self.x, self.y,
            Apple.size, Apple.size
        )
        
        pygame.draw.rect(window, [255, 0, 0], apple_rect)


def render(snake, apple):
    window.fill([0, 0, 0])
    
    snake.draw(window)
    apple.draw(window)
        
    pygame.display.update()


snake = Snake(240, 240)
apple = Apple(random.randint(0, 485), random.randint(0, 485))

is_running = True
while is_running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.x_change = 0
                snake.y_change = -20
            if event.key == pygame.K_a:
                snake.x_change = -20
                snake.y_change = 0
            if event.key == pygame.K_s:
                snake.x_change = 0
                snake.y_change = 20
            if event.key == pygame.K_d:
                snake.x_change = 20
                snake.y_change = 0
                
    snake.move()
            
    if apple.is_eaten(snake):
        snake.length += 1
        apple.x = random.randint(0, 485)
        apple.y = random.randint(0, 485)
        
    if snake.is_out_of_bounds(window):
        pygame.quit()
    
    render(snake, apple)
    clock.tick(15)