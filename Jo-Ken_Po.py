import pygame
import random
import os

pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

tela_altura=600
tela_largura=900
FPS=60

pedra_largura=200
pedra_altura=350

papel_largura=200
papel_altura=350

tesoura_largura=200
tesouraa_altura=350


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

class Pedra(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_pedra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 

class Papel(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_papel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y =

class Tesoura(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_tesoura']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 



