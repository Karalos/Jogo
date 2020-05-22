#init
import pygame,sys,random
pygame.init()

#cores
aqua=(0,255,255)
black=(0,0,0)
blue=(0,0,255)
fuchsia=(255,0,255)
gray=(128,128,128)
dark_gray=(40,40,40)
light_gray=(169,169,169)
green=(0,128,0)
lime=(0,255,0)
marron=(128,0,0)
navy_blue=(0,0,128)
olive=(128,128,0)
purple=(128,0,128)
red=(255,0,0)
silver=(192,192,192)
teal=(0,128,182)
white=(255, 255, 255)
yellow=(255,255,0)
bege=(252,188,122)
verde_claro=(125,222,78)

#dados
sorteio1=random.randint(1,4)
sorteio2=random.randint(1,4)
sorteio3=random.randint(1,4)
sorteio4=random.randint(1,4)

#jogo
    #janela
display=pygame.display.set_mode((1500,850))
display.fill(verde_claro)
title=pygame.display.set_caption("Trabalho 2 de Dessoft")
    #player 


    #tablueiro

    #peca
center=[100,100]
raio=100


    #jogadores
jogadores=['bot1','bot2','bot3','player']

#atualizacao
jogo=True
while jogo:
    for event in pygame.event.get():
        #sair
        if event.type == pygame.QUIT:
            jogo=False



        #animacao
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                center[1]+=100
            if event.key==pygame.K_UP:
                center[1]+=-100
            if event.key==pygame.K_LEFT:
                center[0]+=-100
            if event.key==pygame.K_RIGHT:
                center[0]+=100

        #
    display.fill(verde_claro)
    pygame.draw.rect(display,light_gray,(25,25,150,100))
    pygame.draw.circle(display, blue, center,raio)
    pygame.display.update()
pygame.quit()


def andar(ticks):
    object.x += float(x_speed) * ticks / 1000  # converting to float is needed

# this is your main game loop
time = pygame.time.Clock()
ticks = 0
while jogo:
    ...
    update_object(ticks)
    ticks = time.tick(30) 