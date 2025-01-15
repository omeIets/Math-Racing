import pygame
from sys import exit  # pesquisar função dessa biblioteca !!!

# funcao gerar pergunta e resposta

# funcao calcular movimentaçao do carro

pygame.init()  # inicia o pygame (ajuda a renderizar imagens, tocar sons, etc)
pygame.display.set_caption('Math Racing')
# pygame.display.set_icon()
screen = pygame.display.set_mode((900, 600))  # definir hight and width
screen.fill((44, 43, 43, 1))

# surfaces e rects
carro_ferrari = pygame.image.load('images/carro_ferrari.png').convert_alpha()
carro_ferrari = pygame.transform.rotozoom(carro_ferrari, 0, 0.65)
carro_ferrari_rect = carro_ferrari.get_rect(center=(450, 340))
txt_logo = pygame.image.load('images/txt_logo.png').convert_alpha()
txt_logo = pygame.transform.rotozoom(txt_logo, 0, 0.7)
txt_logo_rect = txt_logo.get_rect(center=(450, 200))
xadrez = pygame.image.load('images/xadrez.png').convert_alpha() 
xadrez = pygame.transform.rotozoom(xadrez, 0, 0.6) # nao fiz rect pq vai ser sempre no 0,0
txt_qualquerbotao = pygame.image.load('images/txt qualquer botao.png').convert_alpha()
txt_qualquerbotao = pygame.transform.rotozoom(txt_qualquerbotao, 0, 0.7)
txt_qualquerbotao_rect = txt_qualquerbotao.get_rect(center=(450, 510))
infos = pygame.image.load('images/icone_informacoes.png').convert_alpha()
infos = pygame.transform.rotozoom(infos, 0, 0.7)
infos_rect = infos.get_rect(center=(800, 120))

carro1 = pygame.image.load('images/carro1.png').convert_alpha()
carro1_rect = carro1.get_rect(midleft=(0, 290))
carro2 = pygame.image.load('images/carro2.png').convert_alpha()
carro2_rect = carro2.get_rect(midleft=(0, 350))

# input_rect = pygame.Rect(100, 100, 140, 32)
# input_color_inactive = pygame.Color('lightskyblue3')
# input_color_active = pygame.Color('dodgerblue2')
# input_color = input_color_inactive
# input_active = False
# text = ''

game_active = False
clock = pygame.time.Clock()

# onde o jogo acontece
while True:

    # checar todos os eventos
    for event in pygame.event.get():  # o metodo capta os eventos e o loop passa por todos eles
        if event.type == pygame.QUIT:  # o mesmo que clicar no botão de x
            pygame.quit()  # pesuisar função certa !!!
            exit()  # uso do sys fecha todo codigo que tiver aberto, o código apenas acaba e fecha a janela
        
        # Se o usuario apertou no input
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if input_rect.collidepoint(event.pos):
        #         input_active = not input_active
        #     else:
        #         input_active = False
        #     input_color = input_color_active if input_active else input_color_inactive
        
        # Salva cada tecla apertada
        # if event.type == pygame.KEYDOWN:
        #     if input_active:
        #         if event.key == pygame.K_RETURN:
        #             # ** Faz o carro andar, passa a vez pro outro, salva resposta e etc **                         
        #             print(text)
        #             text = ''
        #         elif event.key == pygame.K_BACKSPACE:
        #             text = text[:-1]
        #         else:
        #             text += event.unicode

        if game_active:
            screen.blit(carro1,carro_ferrari_rect)
            # pausar jogo com esc e calcular tempo jogo pausado
            # mouse motion para instruções
            ##########
        else:
            # reseta o jogo se apertar qualquer tecla apos endgame
            if event.type == pygame.KEYDOWN:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(carro2,txt_qualquerbotao_rect)
        # tela instruções por x segundos
        # keys = pygame.key.get_pressed()
        # tempo_1 = pygame.time.get_ticks()
        # tempo_2 = pygame.time.get_ticks()

        # player = 1

        # se for turno do player 1
            # chama funcao que gera pergunta e resposta
            
            # RENDERIZANDO O INPUT
            # Render the current text.
            # txt_surface = test_font.render(text, True, input_color)
            # # Resize the box if the text is too long.
            # width = max(200, txt_surface.get_width()+10)
            # input_rect.w = width
            # # Blit the text.
            # screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
            # # Blit the input_box rect.
            # pygame.draw.rect(screen, input_color, input_rect, 2)

            # escreve os dois no txt
            # if keys[pygame.(letra a)]
                # resposta_player = A
            # elif keys[pygame.letra b]
                # resposta_player = B
            # escreve respsot aplayer no txt
            # se resposta usuario for igual a resposta 
                # carrox.left += (chama funcao que usa o tempo do time atual - inicial)
            # tempo_resposta = pygame.time.get_ticks()
            # player = 2

    else:
        screen.blit(txt_logo,txt_logo_rect)
        screen.blit(xadrez,(0,0))
        screen.blit(txt_qualquerbotao,txt_qualquerbotao_rect)
        screen.blit(infos,infos_rect)
        screen.blit(carro_ferrari,carro_ferrari_rect)
            # chama funcao que gera pergunta e resposta
            # escreve os dois no txt
            # if keys[pygame.(letra a)]
                # resposta_player = A
            # elif keys[pygame.letra b]
                # resposta_player = B
            # escreve respsot aplayer no txt
            # se resposta usuario for igual a resposta 
                # carrox.left += (chama funcao que usa o tempo do time atual - inicial)
            # tempo_resposta = pygame.time.get_ticks()
            # player = 1

        ###########
    # else:
        # mostra carro vencedor ou tela inicial se nao tiver vencedor ainda
        # escreve vencedor no txt
        # play again

    # atualiza tudo a cada frame
    pygame.display.update()  # atualiza o display constantemente
    clock.tick(60)  # entender como funciona esse forró
    # tells that the while loop should not run faster than 60 times per second (prevents the game from running too fast)(max framerate)
