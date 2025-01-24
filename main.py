import pygame
import random
from sys import exit


def tocar_audios(audio):
    '''
    essa função auxilia no gerenciamento dos diferentes audios do jogo a serem tocados
    '''
    if audio == 1:
        pygame.mixer.music.load('audios/audio_senna.mp3')
        pygame.mixer.music.set_volume(0.7)
    elif audio == 2:
        pygame.mixer.music.load('audios/musica_tema.mp3')
        pygame.mixer.music.set_volume(0.7)
    elif audio == 3:
        pygame.mixer.music.load('audios/radio.mp3')
    elif audio == 4:
        pygame.mixer.music.load('audios/acerto.mp3')
        pygame.mixer.music.set_volume(0.7)
    elif audio == 5:
        pygame.mixer.music.load('audios/erro.mp3')
        pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

def definir_numeros():
    '''
    essa função gera os números que serão usados nas equações de cada round, retornando:

    num1, num2, num3(int) -> os números a serem usados
    vai_ter_raiz(int) -> indica se algum dos números que vão ser usados na verdade aparecerá
                    na equação como sua raiz (0 para não e 1 para sim)
    xcx(int) -> qual dos 3 números é o que será tirada a raiz (1,2,3 ou então, se não houver, 0)
    raiz_numero(int) -> raiz já calculada do número que será utilizada essa raiz (se houver algum,
                    se não retorna 0)
    '''
    numeros = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    raiz_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indice_numero_com_raiz = random.randint(0, 9)
    numero_que_e_raiz = numeros[indice_numero_com_raiz]
    raiz_numero = raiz_numeros[indice_numero_com_raiz]
    vai_ter_raiz = random.randint(0, 1)

    if vai_ter_raiz == 1:
        xcx = random.randint(1, 3)  # random qual número que vai ter raiz
        if xcx == 1:
            num1 = numero_que_e_raiz
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
        elif xcx == 2:
            num1 = random.randint(1, 10)
            num2 = numero_que_e_raiz
            num3 = random.randint(1, 10)
        else:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num3 = numero_que_e_raiz
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        xcx = raiz_numero = 0
    return num1, num2, num3, vai_ter_raiz, xcx, raiz_numero


def gerar_resultado():
    '''
    essa função é utilizada para realizar todo o cálculo da equação bem como cálculos complementares
    por meio dela que são definidas as operações que a equação conterá
    ela também evita equações que contenham divisões com resultados não exatos
    ela retornará:

    num1,num2,num3(int) -> os mesmos já definidos pela função anterior ou então (se ocorreu divisão não exata)
                      os novos números gerados e utilizados na equação
    resp(int) -> resposta da equação
    operacao1, operacao2(int) -> quais foram as duas operações realizadas na equação (1 = +, 2 = -, 3 = *, 4 = /)
    tem_raiz(int) -> valor retirado direto da função anterior, diz se alguns dos números será utilizado sua raiz
    numero_com_raiz -> valor retirado do "xcx" da função anterior, diz qual dos três números que foi utilizado sua 
                       raiz (se houver algum)
    '''

    operacao1 = random.randint(1, 4)
    operacao2 = random.randint(1, 4)
    num1, num2, num3, tem_raiz, numero_com_raiz, raiz_do_numero = definir_numeros()

    # substituir numero que tem raiz pelo valor da sua raiz
    if numero_com_raiz == 1:
        temp = num1  # guarda numero original
        num1 = raiz_do_numero
    elif numero_com_raiz == 2:
        temp = num2
        num2 = raiz_do_numero
    elif numero_com_raiz == 3:
        temp = num3
        num3 = raiz_do_numero

    # evita contas com divisao sem ser exata
    if operacao1 == 4 and operacao2 == 4:
        # se alguma das operacoes nao da exata gera novos numeros
        while num1 % num2 != 0 or (num1 / num2) % num3 != 0:
            num1, num2, num3, tem_raiz, numero_com_raiz, raiz_do_numero = definir_numeros()
            if numero_com_raiz == 1:  # substitui raizes de novos numeros gerados
                temp = num1
                num1 = raiz_do_numero
            elif numero_com_raiz == 2:
                temp = num2
                num2 = raiz_do_numero
            elif numero_com_raiz == 3:
                temp = num3
                num3 = raiz_do_numero
    elif operacao1 == 4:
        while num1 % num2 != 0:
            num1, num2, num3, tem_raiz, numero_com_raiz, raiz_do_numero = definir_numeros()
            if numero_com_raiz == 1:
                temp = num1
                num1 = raiz_do_numero
            elif numero_com_raiz == 2:
                temp = num2
                num2 = raiz_do_numero
            elif numero_com_raiz == 3:
                temp = num3
                num3 = raiz_do_numero
    elif operacao2 == 4:
        while num2 % num3 != 0:
            num1, num2, num3, tem_raiz, numero_com_raiz, raiz_do_numero = definir_numeros()
            if numero_com_raiz == 1:
                temp = num1
                num1 = raiz_do_numero
            elif numero_com_raiz == 2:
                temp = num2
                num2 = raiz_do_numero
            elif numero_com_raiz == 3:
                temp = num3
                num3 = raiz_do_numero

    # soma
    if operacao1 == 1:
        if operacao1 == 1 and operacao2 == 1:
            # tudo soma
            resp = num1+num2+num3
        elif operacao1 == 1 and operacao2 == 2:
            resp = num1+num2-num3
        elif operacao1 == 1 and operacao2 == 3:
            resp = num1+(num2*num3)
        elif operacao1 == 1 and operacao2 == 4:
            resp = int(num1+(num2/num3))
    # sub
    elif operacao1 == 2:
        if operacao1 == 2 and operacao2 == 1:
            # tudo soma
            resp = num1-num2+num3
        elif operacao1 == 2 and operacao2 == 2:
            resp = num1-num2-num3
        elif operacao1 == 2 and operacao2 == 3:
            resp = num1-(num2*num3)
        elif operacao1 == 2 and operacao2 == 4:
            resp = int(num1-(num2/num3))
    # mult
    elif operacao1 == 3:
        if operacao1 == 3 and operacao2 == 1:
            resp = (num1*num2)+num3
        elif operacao1 == 3 and operacao2 == 2:
            resp = (num1*num2)-num3
        elif operacao1 == 3 and operacao2 == 3:
            resp = num1*num2*num3
        elif operacao1 == 3 and operacao2 == 4:
            resp = int(num1*(num2/num3))
    # div
    elif operacao1 == 4:
        if operacao1 == 4 and operacao2 == 1:
            resp = int((num1/num2)+num3)
        elif operacao1 == 4 and operacao2 == 2:
            resp = int((num1/num2)-num3)
        elif operacao1 == 4 and operacao2 == 3:
            resp = int(num1/num2*num3)
        elif operacao1 == 4 and operacao2 == 4:
            resp = int(num1/num2/num3)

    # retorna ao numero sem a raiz calculada
    if numero_com_raiz == 1:
        num1 = temp
    elif numero_com_raiz == 2:
        num2 = temp
    elif numero_com_raiz == 3:
        num3 = temp

    return num1, num2, num3, resp, operacao1, operacao2, tem_raiz, numero_com_raiz


def gerar_equacao():
    '''
    essa função formata a equação da forma que aparecerá para o usuário 
    ela retornará:

    conta(str) -> a equação formatada na forma de string
    resp(str) -> a resposta da equação na fomra de string, a fim de ser comparada com o input(str)
                do jogador no decorrer do jogo
    '''
    num1, num2, num3, resp, operacao1, operacao2, raiz, num_raiz = gerar_resultado()
    sinais = ['+', '-', '*', '/']

    if raiz:
        if num_raiz == 1:
            conta = f'√{num1} {sinais[operacao1 -1]} {num2} {sinais[operacao2 - 1]} {num3}'
        elif num_raiz == 2:
            conta = f'{num1} {sinais[operacao1 -1]} √{num2} {sinais[operacao2 - 1]} {num3}'
        else:
            conta = f'{num1} {sinais[operacao1 -1]} {num2} {sinais[operacao2 - 1]} √{num3}'
    else:
        conta = f'{num1} {sinais[operacao1 -1]} {num2} {sinais[operacao2 - 1]} {num3}'

    return conta, str(resp)


pygame.init()  # inicia o pygame (ajuda a renderizar imagens, tocar sons, etc)
pygame.display.set_caption('Math Racing')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((900, 600))
screen.fill((44, 43, 43, 1))

# surfaces e rects ////////////////////////////////////////////////

# tela inicial
carro_ferrari = pygame.image.load('images/carro_ferrari.png').convert_alpha()
carro_ferrari = pygame.transform.rotozoom(carro_ferrari, 0, 0.65)
carro_ferrari_rect = carro_ferrari.get_rect(center=(450, 340))
carro_williams = pygame.image.load('images/carro_williams.png').convert_alpha()
carro_williams = pygame.transform.rotozoom(carro_williams, 0, 0.6)
carro_williams_rect = carro_williams.get_rect(center=(450, 320))
xadrez = pygame.image.load('images/xadrez.png').convert_alpha()
# nao fiz rect pq vai ser sempre no 0,0
xadrez = pygame.transform.rotozoom(xadrez, 0, 0.65)
infos = pygame.image.load('images/icone_informacoes.png').convert_alpha()
infos = pygame.transform.rotozoom(infos, 0, 0.7)
infos_rect = infos.get_rect(center=(800, 120))

# jogo
fundo_player1 = pygame.image.load('images/fundo_player1.png')
# fundos nao precisam de convert.alpha nem de rect
fundo_player2 = pygame.image.load('images/fundo_player2.png')
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
txt_fim_corrida = pygame.image.load(
    'images/txt_fim_corrida.png').convert_alpha()
txt_fim_corrida = pygame.transform.rotozoom(txt_fim_corrida, 0, 0.7)
txt_fim_corrida_rect = txt_fim_corrida.get_rect(center=(450, 50))
txt_vencedor_player1 = pygame.image.load(
    'images/txt_vencedor_player1.png').convert_alpha()
txt_vencedor_player1 = pygame.transform.rotozoom(txt_vencedor_player1, 0, 0.6)
txt_vencedor_player2 = pygame.image.load(
    'images/txt_vencedor_player2.png').convert_alpha()
txt_vencedor_player2 = pygame.transform.rotozoom(txt_vencedor_player2, 0, 0.6)
txt_vencedor_player_rect = txt_vencedor_player1.get_rect(center=(450, 210))
txt_jogar_novamente = pygame.image.load(
    'images/txt_jogar_novamente.png').convert_alpha()
txt_jogar_novamente = pygame.transform.rotozoom(txt_jogar_novamente, 0, 0.7)
txt_jogar_novamente_rect = txt_jogar_novamente.get_rect(center=(450, 520))

# Texto Input
text_p1 = ''
text_p2 = ''

# txt_qualquerbotao
opacity = 0
fade_direction = 1  # 1 para aumentar opacidade, -1 para diminuir
fade_speed = 3  # Velocidade de alteração da opacidade

font = pygame.font.Font("fontes/Formula1.otf", 30)
font_contas = pygame.font.Font("fontes/fonte_contas.ttf", 30)
# tocar_audios(2)

game_mode = tempo_inicial = mexer = vencedor = 0
cenarios = int(round((900 / tam_cenario) + 1, 0))
fim = False
clock = pygame.time.Clock()
contar_caracter = False

# onde o jogo acontece
while True:

    # checar todos os eventos
    for event in pygame.event.get():  # o metodo capta os eventos e o loop passa por todos eles
        if event.type == pygame.QUIT:  # o mesmo que clicar no botão de x
            pygame.quit()  # pesuisar função certa !!!
            exit()  # uso do sys fecha todo codigo que tiver aberto, o código apenas acaba e fecha a janela

        if game_mode == 0:  # tela inicial/final
            contar_caracter = False
            screen.blit(carro_ferrari, carro_ferrari_rect)
            # reseta o jogo se apertar qualquer tecla apos endgame
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
                if infos_rect.collidepoint(mouse_pos):
                    tocar_audios(3)
                    game_mode = 2
            if event.type == pygame.KEYDOWN:
                vencedor = 0
                carro_azul_rect = carro_azul.get_rect(midleft=(5, 490))
                carro_vermelho_rect = carro_vermelho.get_rect(midleft=(5, 420)) # reseta posicoes dos carros
                game_mode = 1
                player = 1
                fim = False
                gerar_conta = True  # gera conta para o primeiro player do primeiro round
                tocou = False # tocar audio do vencedor so uma vez
                tempo_inicial = pygame.time.get_ticks()
                pygame.mixer.music.stop()  # para de tocar a musica de fundo

        if game_mode == 1:  # jogo em si

            # # Salva cada tecla apertada
            if player == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if text_p1 == resp:
                            carro_vermelho_rect.left += 30 + \
                                (10 - ((tempo_atual - tempo_inicial) / 1000)) * 10
                            tocar_audios(4)
                        else:
                            tocar_audios(5)

                        text_p1 = ''
                        # comeca a contar o tempo do proximo player a partir do enter do anterior
                        pygame.time.wait(3000)
                        tempo_inicial = tempo_atual + 3000
                        gerar_conta = True  # muda round entao precisa gerar outra conta
                        player = 2
                    elif event.key == pygame.K_BACKSPACE:
                        text_p1 = text_p1[:-1]

                    elif contar_caracter:
                        text_p1 += event.unicode
                    contar_caracter = True

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if text_p2 == resp:
                            carro_azul_rect.left += 30 + \
                                (10 - ((tempo_atual - tempo_inicial) / 1000)) * 10
                            tocar_audios(4)
                        else:
                            tocar_audios(5)
                        text_p2 = ''
                        # comeca a contar o tempo do proximo player a partir do enter do anterior
                        pygame.time.wait(3000)
                        tempo_inicial = tempo_atual + 3000
                        gerar_conta = True  # muda round entao precisa gerar outra conta
                        player = 1

                    elif event.key == pygame.K_BACKSPACE:
                        text_p2 = text_p2[:-1]
                    else:
                        text_p2 += event.unicode

        if game_mode == 2:  # tela instruções
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # se botao do mouse pressionado e a posicao colidir com o rect do botao de infos
                if txt_voltar_rect.collidepoint(mouse_pos):
                    tocar_audios(2)
                    game_mode = 0

    if game_mode == 1:  # jogo em si
        fundo = pygame.Surface((900, 600))
        fundo.fill((44, 43, 43, 1))
        # variaveis de tempo so existem durante game mode 1!!
        tempo_atual = pygame.time.get_ticks()

        # cronometro dos rounds
        timer_round = 10 - ((tempo_atual - tempo_inicial) / 1000)
        if timer_round <= 0:  # quando zera gira os turnos
            if player == 1:
                player = 2
                text_p1 = ''
            else:
                player = 1
                text_p2 = ''
            # reseta tempos pois vai mudar round
            tempo_inicial = tempo_atual = pygame.time.get_ticks()
            gerar_conta = True  # muda round entao precisa gerar outra conta

        # rounds
        if gerar_conta:
            equacao, resp = gerar_equacao()
            gerar_conta = False
        equacao_surface = font_contas.render(f'{equacao}', True, 'white')

        if player == 1:
            screen.blit(fundo_player1, (0, 0))
            screen.blit(seta_esquerda, seta_esquerda_rect)
            # define em que lado da tela vai blitar a conta
            equacao_rect = equacao_surface.get_rect(center=(214, 160))
        else:
            screen.blit(fundo_player2, (0, 0))
            screen.blit(seta_direita, seta_direita_rect)
            equacao_rect = equacao_surface.get_rect(center=(687, 160))

        # ---------------------temporario----------------------
        timer_surf = font.render(f'{timer_round:.2f}', False, 'White')
        if player == 1:
            score_rect = timer_surf.get_rect(center=(214, 105))
        else:
            score_rect = timer_surf.get_rect(center=(687, 105))
        # -----------------------------------------------------

        screen.blit(pista, (0, 0))
        screen.blit(carro_azul, carro_azul_rect)
        screen.blit(carro_vermelho, carro_vermelho_rect)
        screen.blit(timer_surf, score_rect)
        screen.blit(equacao_surface, equacao_rect)

        # cenario se mexendo
        for i in range(0, cenarios):
            screen.blit(cenario, (i * tam_cenario + mexer, 0))
        # variavel mexer
        mexer -= 5
        # resetando a imagem quando chega na borda
        if abs(mexer) > tam_cenario:
            mexer = 0

        # carros passando pela linha de chegada
        if carro_vermelho_rect.right > 840:  # se um dos carros passa o x da linha de chegada
            if not tocou: # toca audio so uma vez
                tocar_audios(1)
                tocou = True
            screen.blit(chegada, (840, 395))  # aparece a linha de chegada
            # blit dnv para nao ficar por baixo da linha de chegada
            screen.blit(carro_vermelho, carro_vermelho_rect)
            carro_vermelho_rect.left += 3  # vai andando o carro
            if carro_vermelho_rect.left > 900:  # quando a bunda do carro passar dos 900 da tela muda o game mode
                game_mode = 0
                vencedor = 1
        elif carro_azul_rect.right > 840:
            if not tocou: # toca audio so uma vez
                tocar_audios(1)
                tocou = True
            screen.blit(chegada, (840, 395))
            screen.blit(carro_azul, carro_azul_rect)
            carro_azul_rect.left += 3
            if carro_azul_rect.left > 900:
                game_mode = 0
                vencedor = 2

        # Render the current text.
        txt_surface = font.render(text_p1, True, 'white')
        screen.blit(txt_surface, (100, 200))
        txt_surface = font.render(text_p2, True, 'white')
        screen.blit(txt_surface, (570, 200))

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
            screen.blit(xadrez, (0, 0))
            screen.blit(infos, infos_rect)
            screen.blit(txt_vencedor_player1, txt_vencedor_player_rect)
            screen.blit(carro_ferrari, carro_ferrari_rect)
            screen.blit(txt_jogar_novamente, txt_jogar_novamente_rect)
            screen.blit (txt_fim_corrida, txt_fim_corrida_rect)
        elif vencedor == 2:
            screen.blit(xadrez, (0, 0))
            screen.blit(infos, infos_rect)
            screen.blit(txt_vencedor_player2, txt_vencedor_player_rect)
            screen.blit(carro_williams, carro_williams_rect)
            screen.blit(txt_jogar_novamente, txt_jogar_novamente_rect)
            screen.blit (txt_fim_corrida, txt_fim_corrida_rect)
        else:
            screen.blit(txt_logo, txt_logo_rect)
            screen.blit(xadrez, (0, 0))
            screen.blit(txt_qualquerbotao, txt_qualquerbotao_rect)
            screen.blit(infos, infos_rect)
            screen.blit(carro_ferrari, carro_ferrari_rect)

        # 231 Atualiza a opacidade do txt_qualquerbotao
        opacity += fade_direction * fade_speed
        if opacity >= 255:  # Inverte a direção ao atingir o máximo
            opacity = 255
            fade_direction = -1
        elif opacity <= 0:  # Inverte a direção ao atingir o mínimo
            opacity = 0
            fade_direction = 1

        txt_qualquerbotao.set_alpha(opacity)
        txt_jogar_novamente.set_alpha(opacity)

    # atualiza tudo a cada frame
    pygame.display.update()  # atualiza o display constantemente
    clock.tick(60)  # entender como funciona esse forró