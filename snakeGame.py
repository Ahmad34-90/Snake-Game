import pygame
pygame.init()

#Colors
white = (255, 255, 255, 1)
black = (0, 0, 0 , 0)

#Game Specific Variable
screen_width =1200
screen_height = 600
snake_x =45
snake_y= 55
snake_size =10
fps = 30             # fps = FramePerSecond

clock = pygame.time.Clock()

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("SnakeWithAhmad")
pygame.display.update()

#Game Specific Variable
exit_game = False
game_over = False

#Game Loop
while not exit_game:
    for event in pygame.event.get():  
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True   

        if event.type == pygame.KEYDOWN:          # Right moment
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10 
            
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10

            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])               #Snake character Creation
    clock.tick(fps)
    pygame.display.update()
pygame.quit() 
exit()