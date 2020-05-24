import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
pasta_img=path.join(path.dirname(__file__), 'imagens')

#variaveis
largura_tela=561
altura_tela=766
FPS=60
#frutas
fruta_largura=100
fruta_altura=76
#cesta
cesta_largura=100
cesta_altura=76
#bota
bota_largura=100
bota_altura=76

#estados
inicio = 0
jogo = 1
fim = 2

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
#########################################################################################################################################################
BACKGROUND = 'background'
IMAG_CESTA = 'imag_cesta'
IMAG_FRUTA = 'imag_fruta'
IMAG_BOTA = 'imag_bota'
PONTUACAO_FONT = 'pontuacao_font'
SOM_ERRO = 'som_erro'
som_acerto = 'som_acerto'

def load_assets():
    assets = {}
    #carrega imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.png')).convert()
    assets[IMAG_CESTA] = pygame.image.load(os.path.join(pasta_img, 'cesta.png')).convert_alpha()
    assets[IMAG_FRUTA] = pygame.image.load(os.path.join(pasta_img, 'maca_verde.png')).convert_alpha()
    assets[IMAG_BOTA] = pygame.image.load(os.path.join(pasta_img, 'bota.png')).convert_alpha()
    #muda dimensoes imagens
    assets[IMAG_CESTA] = pygame.transform.scale(assets['imag_cesta'], (cesta_largura, cesta_altura))
    assets[IMAG_FRUTA] = pygame.transform.scale(assets['imag_fruta'], (fruta_largura, fruta_altura))
    assets[IMAG_BOTA] = pygame.transform.scale(assets['imag_bota'], (bota_largura, bota_altura))

    # SONS
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets

###########################################################################################################################################################