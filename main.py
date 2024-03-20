import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ābolu rījējs')


def draw_snake(snake_rectangles):
    pygame.draw.rect(window, [0, 125, 0], snake_rectangles[-1])
    
    for rectangle in snake_rectangles[:-1]:
        pygame.draw.rect(window, [13, 55, 13], rectangle)


def render(snake_rectangles):
    window.fill([0, 0, 0])
    
    draw_snake(snake_rectangles)
        
    pygame.display.update()

snake_length = 5
snake_x = 240
snake_y = 240
snake_rectangles = [pygame.Rect(snake_x, snake_y, 20, 20)]

is_running = True
while is_running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y -= 20
            if event.key == pygame.K_a:
                snake_x -= 20
            if event.key == pygame.K_s:
                snake_y += 20
            if event.key == pygame.K_d:
                snake_x += 20
    
            snake_rectangles.append(
                pygame.Rect(snake_x, snake_y, 20, 20)
            )
            if len(snake_rectangles) > snake_length:
                snake_rectangles.pop(0)
                
            window_rectangle = window.get_rect()
            if not window_rectangle.contains(snake_rectangles[-1]):
                pygame.quit()
    
    render(snake_rectangles)