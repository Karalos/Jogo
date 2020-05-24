import pygame
import random
import os

# Estabelece a pasta que contem as figuras e sons.
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

#variaveis
tela_largura=561
tela_altura=766
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
#"personagens"
class cesta(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        #Simple base class for visible game objects
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[IMAG_CESTA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = tela_largura / 2
        self.rect.bottom = tela_altura - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Posicao cesta
        self.rect.x += self.speedx
        #Nao sai da tela
        if self.rect.right > tela_largura:
            self.rect.right = tela_largura
        if self.rect.left < 0:
            self.rect.left = 0

class fruta(pygame.sprite.Sprite):
    def __init__(self, assets, botom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[IMAG_FRUTA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, tela_largura-fruta_largura)
        self.rect.y = random.randint(-100, -fruta_altura)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Posicao meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-fruta_largura)
            self.rect.y = random.randint(-100, -fruta_altura)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

class bota(pygame.sprite.Sprite):
    def __init__(self, assets, botom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[IMAG_BOTA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, tela_largura-bota_largura)
        self.rect.y = random.randint(-100, -bota_altura)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Posicao meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-bota_largura)
            self.rect.y = random.randint(-100, -bota_altura)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

######################################################################################################
def abrir_tela(screen):
    clock = pygame.time.Clock()
    # Carrega o fundo
    background = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.png')).convert()
    background_rect = background.get_rect()
    jogando = True
    while jogando:
        #velocidade do jogo
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = fim
                jogando = False

            if event.type == pygame.KEYUP:
                condicao = jogo
                jogando = False

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        # inverte o display.
        pygame.display.flip()

    return condicao
###################################################################################################################

