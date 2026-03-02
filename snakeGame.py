import pygame
pygame.init()

#Colors
white = (255, 255, 255, 1)

screen_width =1200
screen_height = 600
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

    gameWindow.fill(white)
    pygame.display.update()
pygame.quit() 
exit()