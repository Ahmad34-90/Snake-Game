import pygame
import random
pygame.init()

#Colors
white = (255, 255, 255, 1)
black = (0, 0, 0 , 0)
green = (0, 255, 0, 1.0)

#Game Specific Variable
screen_width =900
screen_height = 600
snake_x =45
snake_y= 55
velocity_x = 0
velocity_y = 0
snake_size =10
fps = 30             # fps = FramePerSecond

food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)

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

        # Moments of snake in left, right, up, down
        if event.type == pygame.KEYDOWN:          
            if event.key == pygame.K_RIGHT:
                velocity_x= 10 
                velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0
            
            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    # giving velocity(speed)
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, green, [food_x,food_y, snake_size, snake_size])                  #Food creation
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])               #Snake character Creation
    clock.tick(fps)
    pygame.display.update()
pygame.quit() 
exit()