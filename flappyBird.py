import pygame
pygame.init()

gameWindow = pygame.display.set_mode((1200,500))   #Display setup.

pygame.display.set_caption("Flappy Bird Game!")   #Game Title.

exit_game = False
game_over = False

while not exit_game: #game loop.
    for event in pygame.event.get():  #handling events
        if event.type == pygame.quit():
            exit_game = True

pygame.quit()
exit()