import pygame
import random
import os

preto=(0,0,0)

#origem das imagens
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')
pasta_font=os.path.join(os.path.dirname(__file__), 'fontes')

#parametros
tela_largura=1200
tela_altura=750
FPS=60

background_largura=600
background_altura=450

#forca
#forca vertical
forca_v_coordenadas=(30,10,20,300)
#forca horizontal
forca_h_coordenadas=(10,20,200,20)
#forca corda
forca_corda_coordenadas=(145,20,10,50)

#stickman
#cabeca
cabeca_raio=35
cabeca_espessura=10
cabeca_coordenadas=(150,100)
#corpo
corpo_coordenadas=(145,125,10,100)
#braco_esquerdo
braco_esquerdo_coordenadas=((145,130),(145,140),(95,170),(95,160))
#braco_direito
braco_direito_corcoordenadas=((155,130),(155,140),(215,170),(215,160))
#perna_esquerda
perna_esquerda_coordenadas=((145,225),(145,205),(95,315),(105,315))
#perna_direita
perna_direita_corcoordenadas=((155,225),(155,205),(205,315),(195,315))


#caixa de texto
caixa_texto_coordenadas=0

#caixa letras usadas
caixa_usada_coordenadas=0

#"fases" do jogo
instrucao = 0
jogo = 1
fim = 2

#carregando imagens
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_jokenpo.jpg')).convert()
    assets["fonte_texto"] = pygame.font.Font(os.path.join(pasta_font, 'Destacy.ttf'), 40)
    return assets

#conta erros
erros=0

#inicia jogo
pygame.init()
#cria tela
window = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('Forca')
#loop
game = True
while game:
    #verifica eventos
    for event in pygame.event.get():
        #encerra jogo
        if event.type == pygame.QUIT:
            game = False
        #evento teste
        if event.type== pygame.KEYDOWN:
            erros+=1

    #tela de funco
    window.fill((255,255,0)) 

    #desenha forca   
    pygame.draw.rect(window,preto,forca_h_coordenadas)
    pygame.draw.rect(window,preto,forca_v_coordenadas)

    #desenha stickman
    if erros>0:
        pygame.draw.rect(window,preto,forca_corda_coordenadas)
        pygame.draw.circle(window,preto,cabeca_coordenadas,cabeca_raio,cabeca_espessura)

    if erros >1:
        pygame.draw.rect(window,preto,corpo_coordenadas)

    if erros >2:
        pygame.draw.polygon(window,preto,braco_esquerdo_coordenadas)

    if erros >3:
        pygame.draw.polygon(window,preto,braco_direito_corcoordenadas)

    if erros >4:
        pygame.draw.polygon(window,preto,perna_esquerda_coordenadas)

    if erros >5:  
        pygame.draw.polygon(window,preto,perna_direita_corcoordenadas)
           

    #atualiza desenhos
    pygame.display.update()
#encerra jogos
pygame.quit()  
