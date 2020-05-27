import pygame
import random
import os

# Estabelece a pasta que contem as figuras .
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

#variaveis
    #tela
tela_altura=561
tela_largura=575
FPS=60

    #frutas
fruta_largura=75
fruta_altura=50
numero_frutas=10

    #cesta
cesta_largura=125
cesta_altura=100

    #bota
bota_largura=75
bota_altura=50
numero_botas=0

#velocidade
x_bota_max=2
x_bota_min=-2
y_bota_max=5
y_bota_min=2
x_fruta_max=2
x_fruta_min=-2
y_fruta_max=5
y_fruta_min=2
x_cesta=0
mudanca_velocidade_cesta=10


#estados
inicio = 0
jogo = 1
fim = 2

#cores
preto = (0, 0, 0)

def load_assets():
    assets = {}
    #carrega imagens
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.jpg')).convert()
    assets['imag_cesta'] = pygame.image.load(os.path.join(pasta_img, 'cesta.jpg')).convert_alpha()
    assets['imag_fruta'] = pygame.image.load(os.path.join(pasta_img, 'maca_verde.png')).convert_alpha()
    assets['imag_bota'] = pygame.image.load(os.path.join(pasta_img, 'bota.png')).convert_alpha()
    #muda dimensoes imagens
    assets['imag_cesta'] = pygame.transform.scale(assets['imag_cesta'], (cesta_largura, cesta_altura))
    assets['imag_fruta'] = pygame.transform.scale(assets['imag_fruta'], (fruta_largura, fruta_altura))
    assets['imag_bota'] = pygame.transform.scale(assets['imag_bota'], (bota_largura, bota_altura))

    return assets


#"personagens"
class Cesta(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_cesta']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #determina posicao de inicio
        self.rect.centerx = tela_largura / 2 #centro da tela
        self.rect.bottom = tela_altura  #colado ao chao
        self.speedx = x_cesta #velocidade 
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
        self.image = assets['imag_fruta']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao de inicio
        self.rect.x = random.randint(0, tela_largura-fruta_largura)
        self.rect.y = random.randint(-200, -fruta_altura)
        #velocidade
        self.speedx = random.randint(x_fruta_min, x_fruta_max)
        self.speedy = random.randint(y_fruta_min,y_fruta_max)

    def update(self):
        # Posicao fruta
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-fruta_largura)
            self.rect.y = random.randint(-200, -fruta_altura)
            self.speedx = random.randint(x_fruta_min, x_fruta_max)
            self.speedy = random.randint(y_fruta_min, y_fruta_max)

class Bota(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_bota']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao de inicio
        self.rect.x = random.randint(0, tela_largura-bota_largura)
        self.rect.y = random.randint(-200, -bota_altura)
        #velocidade
        self.speedx = random.randint(x_bota_min, x_bota_max)
        self.speedy = random.randint(y_bota_min, y_bota_max)

    def update(self):
        # posicao bota
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < 0 or self.rect.left >tela_largura:
            self.rect.x = random.randint(0, tela_largura-bota_largura)
            self.rect.y = random.randint(-200, -bota_altura)
            self.speedx = random.randint(x_bota_min, x_bota_max)
            self.speedy = random.randint(y_bota_min, y_bota_max)

def tela_de_instrucoes(tela):
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

        tela.fill(preto)
        tela.blit(background, background_rect)
        pygame.display.flip()

    return condicao

def tela_dentro_do_jogo(window):
    #ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Criando grupos 
    sprites = pygame.sprite.Group()
    frutas = pygame.sprite.Group()
    botas = pygame.sprite.Group()
    groups = {}
    groups['sprites'] = sprites
    groups['frutas'] = frutas
    groups['botas'] = botas

    # Jogador
    jogador = Cesta(groups, assets)
    sprites.add(jogador)

    # Botas
    for i in range(numero_botas):
        bota = Bota(assets)
        sprites.add(bota)
        botas.add(bota)
    # Frutas
    for i in range(numero_frutas):
        fruta = Fruta(assets)
        sprites.add(fruta)
        frutas.add(fruta)

    condicao = True
    keys_down = {}

#loop
    while condicao:
        clock.tick(FPS)
        if not frutas:
            condicao = False
        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = False
            if condicao:
                # Verifica teclas
                if event.type == pygame.KEYDOWN:
                    # Altera velocidade
                    if event.key == pygame.K_LEFT:
                        jogador.speedx -= mudanca_velocidade_cesta
                    if event.key == pygame.K_RIGHT:
                        jogador.speedx += mudanca_velocidade_cesta
                if event.type == pygame.KEYUP:
                    # Altera a velocidade
                    if event.key == pygame.K_LEFT:
                            jogador.speedx =0

                    if event.key == pygame.K_RIGHT:
                            jogador.speedx =0

        #Atualiza o jogo
        sprites.update()

        # Verifica encontro entre cesta e bota
        encontros1 = pygame.sprite.spritecollide(jogador, botas, True, pygame.sprite.collide_mask)
        if len(encontros1) > 0:
            jogador.kill()
            keys_down = {}
            condicao=False

        #verifica encontro entre cesta e frota
        encontros2 = pygame.sprite.spritecollide(jogador, frutas, True, pygame.sprite.collide_mask)
        if len(encontros2) > 0:
            keys_down = {}


        window.fill(preto) 
        window.blit(assets['background'], (0, 0))
        sprites.draw(window)
        pygame.display.update()  

#base
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((tela_altura, tela_largura))
pygame.display.set_caption('Cesta')

#roda o jogo
condicao = inicio
while condicao != fim:
    if condicao == inicio:
        condicao = tela_de_instrucoes(window)
    elif condicao == jogo:
        condicao = tela_dentro_do_jogo(window)
    else:
        condicao = fim
#encerra o jogo
pygame.quit()  