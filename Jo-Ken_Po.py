import pygame
import random
import os

pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

tela_altura=561
tela_largura=575
FPS=60

pedra_largura=75
pedra_altura=50

papel_largura=75
papel_altura=50

tesoura_largura=125
tesouraa_altura=100


instrucao = 0
jogo = 1
fim = 2

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_jokenpo.png')).convert()
    assets['imag_pedra'] = pygame.image.load(os.path.join(pasta_img, 'Pedra.png')).convert_alpha()
    assets['imag_papel'] = pygame.image.load(os.path.join(pasta_img, 'Papel.png')).convert_alpha()
    assets['imag_tesoura'] = pygame.image.load(os.path.join(pasta_img, 'Tesoura.png')).convert_alpha()
    assets['imag_pedra'] = pygame.transform.scale(assets['imag_pedra'], (pedra_largura, pedra_altura))
    assets['imag_papel'] = pygame.transform.scale(assets['imag_papel'], (papel_largura, papel_altura))
    assets['imag_tesoura'] = pygame.transform.scale(assets['imag_tesoura'], (tesoura_largura, tesoura_altura))

    return assets


