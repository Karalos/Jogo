import pygame
import random
import os

# Estabelece a pasta que contem as figuras e sons.
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')
pasta_som=os.path.join(os.path.dirname(__file__), 'sons')
#variaveis
    #tela
tela_altura=561
tela_largura=575
FPS=60
    #frutas
fruta_largura=75
fruta_altura=50
    #cesta
cesta_largura=150
cesta_altura=125
    #bota
bota_largura=75
bota_altura=50

#estados
inicio = 0
jogo = 1
fim = 2

#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#########################################################################################################################################################
BACKGROUND = 'background'
IMAG_CESTA = 'imag_cesta'
IMAG_FRUTA = 'imag_fruta'
IMAG_BOTA = 'imag_bota'
PONTUACAO_FONT = 'pontuacao_font'
SOM_ERRO = 'som_erro'
SOM_ACERTO = 'som_acerto'

def load_assets():
    assets = {}
    #carrega imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.jpg')).convert()
    assets[IMAG_CESTA] = pygame.image.load(os.path.join(pasta_img, 'cesta.jpg')).convert_alpha()
    assets[IMAG_FRUTA] = pygame.image.load(os.path.join(pasta_img, 'maca_verde.png')).convert_alpha()
    assets[IMAG_BOTA] = pygame.image.load(os.path.join(pasta_img, 'bota.png')).convert_alpha()
    #muda dimensoes imagens
    assets[IMAG_CESTA] = pygame.transform.scale(assets['imag_cesta'], (cesta_largura, cesta_altura))
    assets[IMAG_FRUTA] = pygame.transform.scale(assets['imag_fruta'], (fruta_largura, fruta_altura))
    assets[IMAG_BOTA] = pygame.transform.scale(assets['imag_bota'], (bota_largura, bota_altura))

    # SONS
    pygame.mixer.music.load(os.path.join(pasta_som, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.2)
    assets[SOM_ERRO] = pygame.mixer.Sound(os.path.join(pasta_som, 'expl3.wav'))
    assets[SOM_ACERTO] = pygame.mixer.Sound(os.path.join(pasta_som, 'expl6.wav'))
    return assets

###########################################################################################################################################################
#"personagens"
class Cesta(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
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
        #limite tela
        if self.rect.right > tela_largura:
            self.rect.right = tela_largura
        if self.rect.left < 0:
            self.rect.left = 0

class Fruta(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[IMAG_FRUTA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, tela_largura-fruta_largura)
        self.rect.y = random.randint(-200, -fruta_altura)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Posicao fruta
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-fruta_largura)
            self.rect.y = random.randint(-100, -fruta_altura)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

class Bota(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[IMAG_BOTA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, tela_largura-bota_largura)
        self.rect.y = random.randint(-100, -bota_altura)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # posicao bota
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-bota_largura)
            self.rect.y = random.randint(-100, -bota_altura)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

######################################################################################################
def abrir_tela(tela):
    clock = pygame.time.Clock()
    # Carrega o fundo
    background = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
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

        tela.fill(BLACK)
        tela.blit(background, background_rect)
        # inverte o display.
        pygame.display.flip()

    return condicao
###################################################################################################################
def tela_dentro_do_jogo(window):
    #ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Criando grupos 
    todos_sprites = pygame.sprite.Group()
    todas_frutas = pygame.sprite.Group()
    todas_botas = pygame.sprite.Group()
    groups = {}
    groups['todos_sprites'] = todos_sprites
    groups['todas_frutas'] = todas_frutas
    groups['todas_botas'] = todas_botas

    # Jogador
    jogador = Cesta(groups, assets)
    todos_sprites.add(jogador)

    # Botas
    for i in range(4):
        bota = Bota(assets)
        todos_sprites.add(bota)
        todas_botas.add(bota)
    # Frutas
    for i in range(4):
        fruta = Fruta(assets)
        todos_sprites.add(fruta)
        todas_frutas.add(fruta)

    condicao = True

    keys_down = {}

#loop
    pygame.mixer.music.play(loops=-1)
    while condicao:
        clock.tick(FPS)
        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = False
            if condicao:
                # Verifica teclas
                if event.type == pygame.KEYDOWN:
                    # Altera velocidade
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        jogador.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        jogador.speedx += 8
                    if event.key == pygame.K_SPACE:
                        jogador.shoot()
                if event.type == pygame.KEYUP:
                    # Altera a velocidade
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            jogador.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            jogador.speedx -= 8

        #Atualiza o jogo
        todos_sprites.update()

        # Verifica encontro entre cesta e bota
        encontros1 = pygame.sprite.spritecollide(jogador, todas_botas, True, pygame.sprite.collide_mask)
        if len(encontros1) > 0:
            # Toca o som de dano
            assets[SOM_ERRO].play()
            jogador.kill()
            keys_down = {}
            condicao=False

        encontros2 = pygame.sprite.spritecollide(jogador, todas_frutas, True, pygame.sprite.collide_mask)
        if len(encontros2) > 0:
            # Toca o som de dano
            assets[SOM_ACERTO].play()
            keys_down = {}


        window.fill(BLACK) 
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando sprites
        todos_sprites.draw(window)
        pygame.display.update()  
####################################
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((tela_altura, tela_largura))
pygame.display.set_caption('Cesta')

condicao = inicio
while condicao != fim:
    if condicao == inicio:
        condicao = abrir_tela(window)
    elif condicao == jogo:
        condicao = tela_dentro_do_jogo(window)
    else:
        condicao = fim

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados