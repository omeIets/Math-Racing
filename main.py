import pygame
from sys import exit  # pesquisar função dessa biblioteca !!!

# funcao gerar pergunta e resposta

def tocar_audios():
    '''
    essa função auxilia no gerenciamento dos diferentes audios do jogo a serem tocados
    '''
    if audio_tocando == 1:
        pygame.mixer.music.load('audios/audio_senna.mp3')
    if audio_tocando == 2:
        pygame.mixer.music.load('audios/musica_tema.mp3')
    pygame.mixer.music.play()

pygame.init()  # inicia o pygame (ajuda a renderizar imagens, tocar sons, etc)
pygame.display.set_caption('Math Racing')
# pygame.display.set_icon()
screen = pygame.display.set_mode((900, 600))
screen.fill((44, 43, 43, 1))

# surfaces e rects ////////////////////////////////////////////////

# tela inicial
carro_ferrari = pygame.image.load('images/carro_ferrari.png').convert_alpha()
carro_ferrari = pygame.transform.rotozoom(carro_ferrari, 0, 0.65)
carro_ferrari_rect = carro_ferrari.get_rect(center=(450, 340))
carro_williams = pygame.image.load('images/carro_williams.png').convert_alpha()
# nao fiz rect pq posicao é igual a da ferrari
carro_williams = pygame.transform.rotozoom(carro_williams, 8, 1)
xadrez = pygame.image.load('images/xadrez.png').convert_alpha()
# nao fiz rect pq vai ser sempre no 0,0
xadrez = pygame.transform.rotozoom(xadrez, 0, 0.65)
infos = pygame.image.load('images/icone_informacoes.png').convert_alpha()
infos = pygame.transform.rotozoom(infos, 0, 0.7)
infos_rect = infos.get_rect(center=(800, 120))

# jogo
fundo_player1 = pygame.image.load('images/fundo_player1.png')
fundo_player2 = pygame.image.load('images/fundo_player2.png') # fundos nao precisam de convert.alpha nem de rect
carro_azul = pygame.image.load('images/carro_azul.png').convert_alpha()
carro_azul = pygame.transform.rotozoom(carro_azul, 0, 0.1)
carro_azul_rect = carro_azul.get_rect(midleft=(5, 490))
carro_vermelho = pygame.image.load('images/carro_vermelho.png').convert_alpha()
carro_vermelho = pygame.transform.rotozoom(carro_vermelho, 0, 0.1)
carro_vermelho_rect = carro_vermelho.get_rect(midleft=(5, 420))
seta_esquerda = pygame.image.load('images/seta_esquerda.png').convert_alpha()
seta_esquerda = pygame.transform.rotozoom(seta_esquerda, 0, 0.3)
seta_esquerda_rect = seta_esquerda.get_rect(center=(450, 200))
seta_direita = pygame.image.load('images/seta_direita.png').convert_alpha()
seta_direita = pygame.transform.rotozoom(seta_direita, 0, 0.3)
seta_direita_rect = seta_direita.get_rect(center=(450, 200))
pista = pygame.image.load('images/pista.png').convert_alpha()
cenario = pygame.image.load("images/vegetacao.png").convert_alpha()
tam_cenario = cenario.get_width()
chegada = pygame.image.load("images/chegada.png").convert_alpha()

# textos
txt_logo = pygame.image.load('images/txt_logo.png').convert_alpha()
txt_logo = pygame.transform.rotozoom(txt_logo, 0, 0.7)
txt_logo_rect = txt_logo.get_rect(center=(450, 200))
txt_qualquerbotao = pygame.image.load(
    'images/txt qualquer botao.png').convert_alpha()
txt_qualquerbotao = pygame.transform.rotozoom(txt_qualquerbotao, 0, 0.7)
txt_qualquerbotao_rect = txt_qualquerbotao.get_rect(center=(450, 510))
txt_voltar = pygame.image.load('images/botao_voltar.png').convert_alpha()
txt_voltar_rect = txt_voltar.get_rect(center=(70, 40))

# Variáveis de controle de opacidade do txt_qualquerbotao
opacity = 0
fade_direction = 1  # 1 para aumentar opacidade, -1 para diminuir
fade_speed = 3  # Velocidade de alteração da opacidade

# Input
# input_rect = pygame.Rect(100, 100, 140, 32)
# input_color_inactive = pygame.Color('lightskyblue3')
# input_color_active = pygame.Color('dodgerblue2')
# input_color = input_color_inactive
# input_active = False
# text = ''

test_font = pygame.font.Font(None, 50)
audio_tocando = 2
# tocar_audios()

game_mode = vencedor = tempo_inicial = mexer = 0
cenarios = int(round((900 / tam_cenario) + 1, 0))
fim = False
clock = pygame.time.Clock()

# onde o jogo acontece
while True:
    
    # checar todos os eventos
    for event in pygame.event.get():  # o metodo capta os eventos e o loop passa por todos eles
        if event.type == pygame.QUIT:  # o mesmo que clicar no botão de x
            pygame.quit()  # pesuisar função certa !!!
            exit()  # uso do sys fecha todo codigo que tiver aberto, o código apenas acaba e fecha a janela

        if game_mode == 0:  # tela inicial/final
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
                tempo_inicial = pygame.time.get_ticks()

        if game_mode == 1:  # jogo em si
            # pausar jogo com esc e calcular tempo jogo pausado

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
                        carro_vermelho_rect.left += 10 + \
                            (10 - ((tempo_atual - tempo_inicial) / 1000)) * 4
                        # da pra por movimentacao para baixo e la usa o timer
                        player = 2
                        # comeca a contar o tempo do proximo player a partir do enter do anterior
                        tempo_inicial = tempo_atual
                        # conta a partir do frame anterior mas como a gente n vai usar muita precisao na mecanica de andar nao faz muita diferença

                        # ** Faz o carro andar, passa a vez pro outro, salva resposta e etc **
                        #             print(text)
                        #             text = ''
                        #         elif event.key == pygame.K_BACKSPACE:
                        #             text = text[:-1]
                        #         else:
                        #             text += event.unicode

                        # tempo_2 = pygame.time.Clock()

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        carro_azul_rect.left += 10 + \
                            (10 - ((tempo_atual - tempo_inicial) / 1000)) * 4
                        player = 1
                        # comeca a contar o tempo do proximo player a partir do enter do anterior
                        tempo_inicial = tempo_atual

        if game_mode == 2:  # tela instruções
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
                if txt_voltar_rect.collidepoint(mouse_pos):
                    game_mode = 0

    if game_mode == 1:  # jogo em si
        fundo = pygame.Surface((900, 600))
        fundo.fill((44, 43, 43, 1))
        tempo_atual = pygame.time.get_ticks() # variaveis de tempo so existem durante game mode 1!!

        # cronometro dos rounds
        timer_round = 10 - ((tempo_atual - tempo_inicial) / 1000)
        if timer_round <= 0: # quando zera gira os turnos
            if player == 1:
                player = 2
            else:
                player = 1
            # reseta tempos pois vai mudar round
            tempo_inicial = tempo_atual = pygame.time.get_ticks()
            
        # rounds
        if player == 1:
            screen.blit(fundo_player1, (0, 0))
            screen.blit(seta_esquerda, seta_esquerda_rect)
            # chama funcao contas
            # blit contas e etc
        else:
            screen.blit(fundo_player2, (0, 0))
            screen.blit(seta_direita, seta_direita_rect)
            # chama funcao contas
            # blit contas e etc

        # ---------------------temporario----------------------
        timer_surf = test_font.render( f'{timer_round:.2f}', False, 'White')  
        if player == 1:
            score_rect = timer_surf.get_rect(center=(214, 105))
        else:
            score_rect = timer_surf.get_rect(center=(687, 105))
        # -----------------------------------------------------

        screen.blit(pista,(0,0))
        screen.blit(carro_azul, carro_azul_rect)
        screen.blit(carro_vermelho, carro_vermelho_rect)
        screen.blit(timer_surf, score_rect)
            

        #cenario se mexendo
        for i in range(0, cenarios):
            screen.blit(cenario, (i * tam_cenario + mexer, 0))
        #variavel mexer
        mexer -= 5
        #resetando a imagem quando chega na borda
        if abs(mexer) > tam_cenario:
            mexer = 0

        # carros passando pela linha de chegada
        if carro_vermelho_rect.right > 840: # se um dos carros passa o x da linha de chegada
            if audio_tocando != 1: # toca audio so uma vez
                audio_tocando = 1
                tocar_audios()
            screen.blit(chegada,(840,395)) # aparece a linha de chegada
            screen.blit(carro_vermelho, carro_vermelho_rect) # blit dnv para nao ficar por baixo da linha de chegada
            carro_vermelho_rect.left += 3 # vai andando o carro
            if carro_vermelho_rect.left > 900: # quando a bunda do carro passar dos 900 da tela muda o game mode
                game_mode = 0
                vencedor = 1
        elif carro_azul_rect.right > 840:
            if audio_tocando != 1:
                audio_tocando = 1
                tocar_audios()
            screen.blit(chegada,(840,395))
            screen.blit(carro_azul, carro_azul_rect)
            carro_azul_rect.left += 3
            if carro_azul_rect.left > 900:
                game_mode = 0
                vencedor = 2


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


    elif game_mode == 2:  # tela instruções
        fundo = pygame.Surface((900, 600))
        fundo.fill('Blue')
        screen.blit(fundo, (0, 0))

        screen.blit(txt_voltar, txt_voltar_rect)

    else:  # tela final/inicial
        fundo = pygame.Surface((900, 600))
        fundo.fill((44, 43, 43, 1))
        screen.blit(fundo, (0, 0))

            # mostrar carro vencedor e tela jogar de novo
        if vencedor == 1:
            screen.blit(carro_ferrari, carro_ferrari_rect)
        elif vencedor == 2:
            screen.blit(carro_williams, carro_ferrari_rect)
                # screen.blit(carro_williams, carro_ferrari_rect)
        else:
            screen.blit(txt_logo, txt_logo_rect)
            screen.blit(xadrez, (0, 0))
            screen.blit(txt_qualquerbotao, txt_qualquerbotao_rect)
            screen.blit(infos, infos_rect)
            screen.blit(carro_ferrari, carro_ferrari_rect)

            #231 Atualiza a opacidade do txt_qualquerbotao
            opacity += fade_direction * fade_speed
            if opacity >= 255:  # Inverte a direção ao atingir o máximo
                opacity = 255
                fade_direction = -1
            elif opacity <= 0:  # Inverte a direção ao atingir o mínimo
                opacity = 0
                fade_direction = 1

            txt_qualquerbotao.set_alpha(opacity)


    # atualiza tudo a cada frame
    pygame.display.update()  # atualiza o display constantemente
    clock.tick(60)  # entender como funciona esse forró
    # tells that the while loop should not run faster than 60 times per second (prevents the game from running too fast)(max framerate)
