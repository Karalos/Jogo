from random import randint
import pygame
from os import path

def CASA3(screen):
    pasta_img=path.join(path.dirname(__file__), 'imagens')
    background1 = pygame.image.load(path.join(pasta_img,"CASA3.png")).convert()
    pygame.display.set_caption('CASA3')
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
    pergunta1=randint(1,3)
    if pergunta1==1:
        numero='Qual a teoria evolucionista adotada hoje?'
        numero1='Darwinismo'
        acao1='eror'
        numero2='Lamarckismo'
        acao2='eror'
        numero3='Neodarwinismo'
        acao3='certa'
        numero4='Fixismo'
        acao4='eror'
        posicao=(80,105)
    elif pergunta1==2:
        numero='C6H14 + (19/2)O2 =?'
        numero1='6CO2 + 7H2O'
        acao1='certa'
        numero2='2(C3H7O8)+O3'
        acao2='eror'
        numero3='Não reage'
        acao3='eror'
        numero4='3(C4H4O6)'
        acao4='eror'
        posicao=(300,105)
    elif pergunta1==3:
        numero='6° planeta do sistema solar?'
        numero1='Jupíter'
        acao1='eror'
        numero2='Urano'
        acao2='eror'
        numero3='Venûs'
        acao3='eror'
        numero4='Saturno'
        acao4='certa'
        posicao=(175,105)
    vert1=[(70,75),(930,75),(930,175),(70,175)]
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
    def button(x,y,l,h,ci,ca,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+l>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(screen,ca,(x,y,l,h))
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
        if seg==0:
            running=False
        now=pygame.time.get_ticks()
        if now-tempo>=contador:
            seg-=1
            contador+=1000
        screen.blit(background1, (0, 0))      
        pygame.draw.polygon(screen,(0,0,0), vert1)
        botao1=button(120,300,325,55,(150,0,0),(250,0,0),acao1) 
        botao2=button(570,300,325,55,(150,0,0),(250,0,0),acao2)
        botao3=button(570,450,325,55,(150,0,0),(250,0,0),acao3)
        botao4=button(120,450,325,55,(150,0,0),(250,0,0),acao4)
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
        screen.blit(resposta1,(125,307))
        screen.blit(resposta2,(575,307))
        screen.blit(resposta3,(575,457))
        screen.blit(resposta4,(125,457))
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
