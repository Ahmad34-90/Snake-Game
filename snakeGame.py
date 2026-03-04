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
init_velocity = 5
fps = 40             # fps = FramePerSecond
score = 0

food_x = random.randint(20, screen_width )
food_y = random.randint(20, screen_height)

clock = pygame.time.Clock()

#Showing score on screen
font = pygame.font.SysFont(None, 50)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("SnakeWithAhmad")
pygame.display.update()

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size]) 
snk_list = [] 
snk_length = 1

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
                velocity_x= init_velocity
                velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    # giving velocity(speed)
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) <6:
        score +=1 

        food_x = random.randint(20, screen_width)
        food_y = random.randint(20, screen_height)

        snk_length += 5


    gameWindow.fill(white)
    text_screen("Score: "+ str(score * 1), green, 5, 5)
    pygame.draw.rect(gameWindow, green, [food_x,food_y, snake_size, snake_size])                  #Food creation

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])               #Snake character Creation
    plot_snake(gameWindow, black, snk_list, snake_size)
    clock.tick(fps)
    pygame.display.update()
pygame.quit() 
exit()