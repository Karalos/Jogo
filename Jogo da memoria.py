import pygame
import random
import os

pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

#variaveis
    #tela
tela_altura=561
tela_largura=600
FPS=60

    #cartas 
carta_largura=75
carta_altura=50
numero_cartas=4

#assets
def load_assets():
    assets = {}
    #carrega imagens
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.jpg')).convert()
    assets['imag_carta_frente'] = pygame.image.load(os.path.join(pasta_img, 'carta_frente.jpg')).convert_alpha()
    assets['imag_carta_tras'] = pygame.image.load(os.path.join(pasta_img, 'carta_tras.png')).convert_alpha()
    #muda dimensoes imagens
    assets['imag_carta_frente'] = pygame.transform.scale(assets['imag_carta_frente'], (carta_largura, carta_altura))
    assets['imag_carta_tras'] = pygame.transform.scale(assets['imag_carta_tras'], (carta_largura, carta_altura))

class Carta(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_carta_tras']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

