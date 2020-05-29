import pygame
import random
import os

#origem das imagens
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')
pasta_font=os.path.join(os.path.dirname(__file__), 'fontes')

#parametros
tela_largura=600
tela_altura=900
FPS=60

background_largura=600
background_altura=450

#stickman
#cabeca
cabeca_raio=
cabeca_cor=
cabeca_espessura=
cabeca_cordenadas=

#corpo
corpo_coordenadas=
corpo_cor=

#braco_esquerdo
braco_esquerdo_coordenadas=
braco_esquerdo_cor=

#braco_direito
braco_direito_corcoordenadas=
braco_direito_corcor=

#perna_esquerda
perna_esquerdo_coordenadas=
perna_esquerdo_cor=

#perna_direita
perna_direito_corcoordenadas=
perna_direito_corcor=

#caixa de texto
caixa_texto_coordenadas=

#caixa letras usadas
caixa_usada_coordenadas=

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
    