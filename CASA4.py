from random import randint
import pygame
from os import path
#funçao principal do casa
def CASA4(screen):
    #importa a tela de fundo
    pasta_img=path.join(path.dirname(__file__), 'imagens')
    background1 = pygame.image.load(path.join(pasta_img,"Casa4.jpg")).convert()
    pygame.display.set_caption('CASA4')
    # define os prerequisitos para se imprimir algo na tela
    fontdado= pygame.font.SysFont(None,90)
    fonte=pygame.font.SysFont(None,60)
    fonteres= pygame.font.SysFont(None,230)
    fonteres2=pygame.font.SysFont(None,150)
    seg=10
    contador=1000
    tempo=pygame.time.get_ticks()
    clock=pygame.time.Clock()
    FPS1 = 20
    acao1=0
    acao2=0
    acao3=0
    acao4=0
    running=True
    # sortei uma das tres perguntas
    pergunta1=randint(1,3)
    if pergunta1==1:
        numero='Maior vencedor do OSCAR?'
        numero1='DiCaprio'
        acao1='eror'
        numero2='Tony Ramos'
        acao2='eror'
        numero3='Walt Dysney'
        acao3='certa'
        numero4='Alan Menken'
        acao4='eror'
        posicao=(240,105)
    elif pergunta1==2:
        numero='Maior bilheteria da história?'
        numero1='Titanic'
        acao1='eror'
        numero2='Ving.:Ultimato'
        acao2='certa'
        numero3='Avatar'
        acao3='eror'
        numero4='Vingadores'
        acao4='eror'
        posicao=(230,105)
    elif pergunta1==3:
        numero='Filme brasileiro de maior bilheteria?'
        numero1='Tropa de elite 2'
        acao1='eror'
        numero2='Tropa de elite 1'
        acao2='eror'
        numero3='Cidade de Deus'
        acao3='eror'
        numero4='Nada a perder'
        acao4='certa'
        posicao=(140,105)
    # muda oq vai imprimir de acordo com a escolhida
    vert1=[(120,75),(880,75),(880,175),(120,175)]
    PERGUNTA1=fonte.render((numero),True,(255,0,0))
    resposta1=fonte.render((numero1),True,(0,0,0))
    resposta2=fonte.render((numero2),True,(0,0,0))
    resposta3=fonte.render((numero3),True,(0,0,0))
    resposta4=fonte.render((numero4),True,(0,0,0))
    acertou=fonteres.render(('ACERTOU'),True,(200,200,0))
    errou=fonteres.render(('ERROU'),True,(200,200,0))
    Tl1=fonteres.render(('TEMPO'),True,(200,200,0))
    Tl2=fonteres.render(('ESGOTADO'),True,(200,200,0))
    acertou1=None
    state=''
    #cria a funçao do botao
    def button(x,y,l,h,ci,ca,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+l>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(screen,ca,(x,y,l,h))
            #define a area de controle do botao
            if click[0]==1 and action!=None:
                if action=='eror':
                    return False
                elif action=='certa':
                    return True
        else:
            pygame.draw.rect(screen,ci,(x,y,l,h))
    while running==True:
        clock.tick(FPS1) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                running = False
                #define se vai jogar o dado de novo ou nao
                flow='repita'
        #coloca o limite de tempo
        if seg==0:
            running=False
        now=pygame.time.get_ticks()
        #faz o contador
        if now-tempo>=contador:
            seg-=1
            contador+=1000
        screen.blit(background1, (0, 0))  
        #cria os bottoes
        pygame.draw.polygon(screen,(0,0,0), vert1)
        botao1=button(150,300,325,55,(150,0,0),(250,0,0),acao1) 
        botao2=button(570,300,325,55,(150,0,0),(250,0,0),acao2)
        botao3=button(570,450,325,55,(150,0,0),(250,0,0),acao3)
        botao4=button(150,450,325,55,(150,0,0),(250,0,0),acao4)
        #define se a natureza do botao
        if not botao1 is None:
            if botao1==True:
                state='certo'
            else:
                state='errado'
        elif botao1 is None and seg==0:
            state='TL'
        if not botao2 is None:
            if botao2==True:
                state='certo'
            else:
                state='errado'
        elif botao2 is None and seg==0:
            state='TL'
        if not botao3 is None:
            if botao3==True:
                state='certo'
            else:
                state='errado'
        elif botao3 is None and seg==0:
            state='TL'
        if not botao4 is None:
            if botao4==True:
                state='certo'
            else:
                state='errado'
        elif botao4 is None and seg==0:
            state='TL'
        screen.blit(resposta1,(155,307))
        screen.blit(resposta2,(575,307))
        screen.blit(resposta3,(570,457))
        screen.blit(resposta4,(155,457))
        #mostra na tela se acertou ou nao
        if state=='certo':
            screen.blit(acertou,(120,250))
            flow='continue'
            pygame.time.wait(3000)
            seg=0
        if state=='errado':
            screen.blit(errou,(220,250))
            flow='repita'
            pygame.time.wait(3000)
            seg=0
        if state=='TL':
            screen.blit(Tl1,(210,220))
            flow='repita'
            screen.blit(Tl2,(90,380))
            pygame.time.wait(3000)
        screen.blit(PERGUNTA1, posicao)
        screen.blit(fonte.render('TEMPO: '+str(seg),True,(255,0,0)),(10,20))
        pygame.display.update() 
    return flow
