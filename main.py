import pygame
from sys import exit # pesquisar função dessa biblioteca !!!

pygame.init()  # inicia o pygame (ajuda a renderizar imagens, tocar sons, etc)
pygame.display.set_caption('Math Racing')
# pesquisar adicionar icon na janela !!!
screen = pygame.display.set_mode((1020, 580)) # definir hight and width
screen.fill ((44, 43, 43, 1))

game_active = False

# onde o jogo acontece
while True:

    # checar todos os eventos
    for event in pygame.event.get(): # o metodo capta os eventos e o loop passa por todos eles
        if event.type == pygame.QUIT: # o mesmo que clicar no botão de x
            pygame.quit() # pesuisar função certa !!!
            exit() # uso do sys fecha todo codigo que tiver aberto, o código apenas acaba e fecha a janela

        if game_active:
            ##########
        else:
            # reseta o jogo se apertar qualquer tecla apos endgame
            if event.type == pygame.KEYDOWN:
                game_active = True
        

    if game_active:
        ###########
    else:
        ###########

    #atualiza tudo a cada frame
    pygame.display.update() # atualiza o display constantemente
    clock.tick(60) # entender como funciona esse forró
    # tells that the while loop should not run faster than 60 times per second (prevents the game from running too fast)(max framerate)