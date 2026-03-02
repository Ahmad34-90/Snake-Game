import pygame
pygame.init()

gameWindow = pygame.display.set_mode((1200,500))   #Display setup.

pygame.display.set_caption("Flappy Bird Game!")   #Game Title.

exit_game = False
game_over = False

#Game loop....
while not exit_game: 
    for event in pygame.event.get():        #handling events...
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                print("You have pressed right key of KeyBoard.")
            if event.key == pygame.K_UP:
                print("You have pressed Up key.")

pygame.quit()
exit()