import pygame
from sys import exit  # pesquisar função dessa biblioteca !!!

# funcao gerar pergunta e resposta

# funcao calcular movimentaçao do carro
# def movimentacao(segundos):

# funcao cronometro
# def cronometro(start_time):
# current_time = int(pygame.time.get_ticks() / 1000) - start_time
# score_surf = test_font.render(f'Score: {current_time}', False, 'White')
# score_rect = score_surf.get_rect(center=(510, 50))
# screen.blit(score_surf, score_rect)
# return current_time

pygame.init()  # inicia o pygame (ajuda a renderizar imagens, tocar sons, etc)
pygame.display.set_caption('Math Racing')
# pygame.display.set_icon()
screen = pygame.display.set_mode((900, 600))
screen.fill((44, 43, 43, 1))

# surfaces e rects
carro_ferrari = pygame.image.load('images/carro_ferrari.png').convert_alpha()
carro_ferrari = pygame.transform.rotozoom(carro_ferrari, 0, 0.65)
carro_ferrari_rect = carro_ferrari.get_rect(center=(450, 340))
carro_williams = pygame.image.load('images/carro_williams.png').convert_alpha()
# nao fiz rect pq posicao é igual a da ferrari
carro_williams = pygame.transform.rotozoom(carro_williams, 8, 1)
xadrez = pygame.image.load('images/xadrez.png').convert_alpha()
# xadrez.set_colorkey((255,255,255))
# nao fiz rect pq vai ser sempre no 0,0
xadrez = pygame.transform.rotozoom(xadrez, 0, 0.65)
infos = pygame.image.load('images/icone_informacoes.png').convert_alpha()
infos = pygame.transform.rotozoom(infos, 0, 0.7)
infos_rect = infos.get_rect(center=(800, 120))
seta_esquerda = pygame.image.load('images/seta_esquerda.png').convert_alpha()
seta_esquerda = pygame.transform.rotozoom(seta_esquerda, 0, 0.3)
seta_esquerda_rect = seta_esquerda.get_rect(center=(450, 200))
seta_direita = pygame.image.load('images/seta_direita.png').convert_alpha()
seta_direita = pygame.transform.rotozoom(seta_direita, 0, 0.3)
seta_direita_rect = seta_direita.get_rect(center=(450, 200))


txt_logo = pygame.image.load('images/txt_logo.png').convert_alpha()
txt_logo = pygame.transform.rotozoom(txt_logo, 0, 0.7)
txt_logo_rect = txt_logo.get_rect(center=(450, 200))
txt_qualquerbotao = pygame.image.load(
    'images/txt qualquer botao.png').convert_alpha()
txt_qualquerbotao = pygame.transform.rotozoom(txt_qualquerbotao, 0, 0.7)
txt_qualquerbotao_rect = txt_qualquerbotao.get_rect(center=(450, 510))
txt_voltar = pygame.image.load('images/botao_voltar.png').convert_alpha()
txt_voltar_rect = txt_voltar.get_rect(center=(70, 40))


carro1 = pygame.image.load('images/carro1.png').convert_alpha()
carro1_rect = carro1.get_rect(midleft=(0, 290))
carro2 = pygame.image.load('images/carro2.png').convert_alpha()
carro2_rect = carro2.get_rect(midleft=(0, 350))

input_rect = pygame.Rect(100, 100, 140, 32)
input_color_inactive = pygame.Color('lightskyblue3')
input_color_active = pygame.Color('dodgerblue2')
input_color = input_color_inactive
input_active = False
text = ''

game_mode = vencedor = 0
fim = False
clock = pygame.time.Clock()
# start_time = 0

# onde o jogo acontece
while True:

    # checar todos os eventos
    for event in pygame.event.get():  # o metodo capta os eventos e o loop passa por todos eles
        if event.type == pygame.QUIT:  # o mesmo que clicar no botão de x
            pygame.quit()  # pesuisar função certa !!!
            exit()  # uso do sys fecha todo codigo que tiver aberto, o código apenas acaba e fecha a janela

        if game_mode == 1:  # jogo em si
            # pausar jogo com esc e calcular tempo jogo pausado
            # mouse motion para instruções

            # Se o usuario apertou no input
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if input_rect.collidepoint(event.pos):
            #         input_active = not input_active
            #     else:
            #         input_active = False
            #     input_color = input_color_active if input_active else input_color_inactive

            # # Salva cada tecla apertada
            if player == 1:
                if event.type == pygame.KEYDOWN:
                    #     if input_active:
                    if event.key == pygame.K_RETURN:
                        player = 2
                        # ** Faz o carro andar, passa a vez pro outro, salva resposta e etc **
                        #             print(text)
                        #             text = ''
                        #         elif event.key == pygame.K_BACKSPACE:
                        #             text = text[:-1]
                        #         else:
                        #             text += event.unicode

                        # carro1_rect.left += movimentacao(int(tempo_1/1000))
                        # tempo_2 = pygame.time.Clock()

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # carro2_rect.left += movimentacao(int(tempo_1/1000))
                        player = 1
            ##########

        if game_mode == 2:  # tela instruções
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
                if txt_voltar_rect.collidepoint(mouse_pos):
                    game_mode = 0
            ##########
        else:  # tela inicial/final
            screen.blit(carro_ferrari, carro_ferrari_rect)
            # reseta o jogo se apertar qualquer tecla apos endgame
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
                if infos_rect.collidepoint(mouse_pos):
                    game_mode = 2
            if event.type == pygame.KEYDOWN:
                game_mode = 1
                player = 1
                fim = False
            #     tempo_1 = pygame.time.Clock()

    if game_mode == 1:  # jogo em si
        fundo = pygame.Surface((900, 600))
        fundo.fill('Yellow')
        screen.blit(fundo, (0, 0))

        if not fim:
            if player == 1:
                screen.blit(seta_esquerda, seta_esquerda_rect)
            else:
                screen.blit(seta_direita, seta_direita_rect)
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

    elif game_mode == 2:  # tela instruções
        fundo = pygame.Surface((900, 600))
        fundo.fill('Blue')
        screen.blit(fundo, (0, 0))

        screen.blit(txt_voltar, txt_voltar_rect)
        #########
        # mouse_buttoms = pygame.mouse.get_pressed() # retorna booleano
        #     if mouse_buttoms:
        #         mouse_pos = pygame.mouse.get_pos()
        #         if bota_voltar.collidepoint(mouse_pos): # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
        #             game_mode = 2

    else:  # tela final/inicial
        fundo = pygame.Surface((900, 600))
        fundo.fill((44, 43, 43, 1))
        screen.blit(fundo, (0, 0))

        if fim:
            # mostrar carro vencedor e tela jogar de novo
            if vencedor == 1:
                screen.blit(carro_ferrari, carro_ferrari_rect)
            else:
                screen.blit(carro_williams, carro_ferrari_rect)
                # screen.blit(carro_williams, carro_ferrari_rect)
                #
        else:
            screen.blit(txt_logo, txt_logo_rect)
            screen.blit(xadrez, (0, 0))
            screen.blit(txt_qualquerbotao, txt_qualquerbotao_rect)
            screen.blit(infos, infos_rect)
            screen.blit(carro_ferrari, carro_ferrari_rect)

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
        # mostra carro vencedor ou tela inicial se nao tiver vencedor ainda
        # escreve vencedor no txt
        # play again

    # atualiza tudo a cada frame
    pygame.display.update()  # atualiza o display constantemente
    clock.tick(60)  # entender como funciona esse forró
    # tells that the while loop should not run faster than 60 times per second (prevents the game from running too fast)(max framerate)
