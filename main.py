import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ābolu rījējs')


class Snake:
    """klase Čūska apraksta čūskas, kā tās izskatās
    un darbojas"""
    
    def __init__(self, x, y):
        """init metodē apraksta objekta īpašības jeb atribūtus"""
        self.length = 5
        self.x = x
        self.y = y
        self.rectangles = [pygame.Rect(self.x, self.y, 20, 20)]

    def move(self):
        self.rectangles.append(
            pygame.Rect(self.x, self.y, 20, 20)
        )
        if len(self.rectangles) > self.length:
            self.rectangles.pop(0) 

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


def render(snake):
    window.fill([0, 0, 0])
    
    snake.draw(window)
        
    pygame.display.update()


snake = Snake(240, 240)

is_running = True
while is_running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.y -= 20
            if event.key == pygame.K_a:
                snake.x -= 20
            if event.key == pygame.K_s:
                snake.y += 20
            if event.key == pygame.K_d:
                snake.x += 20
                
            snake.move()
    
    render(snake)