from random import randint
import pygame
from os import path
def CASA8(screen):
    background1 = pygame.image.load("Casa8.jpg").convert()
    pygame.display.set_caption('CASA8')
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
        numero='Tratado mais duradouro do mundo?'
        numero1='Tordesilhas'
        acao1='eror'
        numero2='Kyoto'
        acao2='eror'
        numero3='Windsor'
        acao3='certa'
        numero4='Berlim'
        acao4='certa'
        posicao=(135,105)
    elif pergunta1==2:
        numero='Quem descobriu a Austrália?'
        numero1='Cabral'
        acao1='eror'
        numero2='Colombo'
        acao2='eror'
        numero3='Darwin'
        acao3='eror'
        numero4='James Cook'
        acao4='certa'
        posicao=(200,105)
    elif pergunta1==3:
        numero='Ano do descobrimento do Brasil?'
        numero1='1500'
        acao1='certa'
        numero2='1501'
        acao2='eror'
        numero3='1499'
        acao3='eror'
        numero4='1502'
        acao4='eror'
        posicao=(170,105)
    vert1=[(125,75),(875,75),(875,175),(125,175)]
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
                JOG8=False
        if seg==0:
            running=False
            JOG8=False
        now=pygame.time.get_ticks()
        if now-tempo>=contador:
            JOG8=True
            seg-=1
            contador+=1000
        screen.blit(background1, (0, 0))      
        pygame.draw.polygon(screen,(0,0,0), vert1)
        botao1=button(150,300,250,55,(150,0,0),(250,0,0),acao1) 
        botao2=button(570,300,250,55,(150,0,0),(250,0,0),acao2)
        botao3=button(570,450,250,55,(150,0,0),(250,0,0),acao3)
        botao4=button(150,450,250,55,(150,0,0),(250,0,0),acao4)
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
        screen.blit(resposta2,(570,307))
        screen.blit(resposta3,(570,457))
        screen.blit(resposta4,(155,457))
        if state=='certo':
            screen.blit(acertou,(120,250))
            pygame.time.wait(3000)
            seg=0
        if state=='errado':
            screen.blit(errou,(220,250))
            pygame.time.wait(3000)
            seg=0
        if state=='TL':
            screen.blit(Tl1,(210,220))
            screen.blit(Tl2,(90,380))
            pygame.time.wait(3000)
        screen.blit(PERGUNTA1, posicao)
        screen.blit(fonte.render('TEMPO: '+str(seg),True,(255,0,0)),(10,20))
        pygame.display.update() 
    return JOG8