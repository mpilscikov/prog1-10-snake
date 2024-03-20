import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ābolu rījējs')


def render(snake):
    window.fill([0, 0, 0])
    
    pygame.draw.rect(window, [0, 125, 0], snake)
    
    pygame.display.update()


snake_x = 240
snake_y = 240

is_running = True
while is_running:
    snake = pygame.Rect(snake_x, snake_y, 20, 20)
    
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
    
    render(snake)