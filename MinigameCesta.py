import pygame
import random
import os

# Estabelece a pasta que contem as figuras .
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

#variaveis
    #tela
tela_altura=600
tela_largura=1100
FPS=60

    #frutas
fruta_largura=120
fruta_altura=80
numero_frutas=4

    #cesta
cesta_largura=125
cesta_altura=100

    #bota
bota_largura=120
bota_altura=80
numero_botas=4

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
instrucao = 0
jogo = 1
fim = 2

#cores
preto = (0, 0, 0)

def load_assets():
    assets = {}
    #carrega imagens
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_cesta.jpg')).convert()
    assets['imag_cesta'] = pygame.image.load(os.path.join(pasta_img, 'cesta.png')).convert_alpha()
    assets['imag_fruta'] = pygame.image.load(os.path.join(pasta_img, 'maca_verde.png')).convert_alpha()
    assets['imag_bota'] = pygame.image.load(os.path.join(pasta_img, 'bota.png')).convert_alpha()
    #muda dimensoes imagens
    #assets['background'] = pygame.transform.scale(assets['background'], (background_largura, background_altura))
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
        self.rect.bottom = tela_altura  
        self.speedx = x_cesta #velocidade 
        self.groups = groups
        self.assets = assets

    def update(self):
        # Posicao cesta
        self.rect.x += self.speedx
        #limite tela
        if self.rect.right < tela_largura/2-230:
            self.rect.right = tela_largura/2-230
        if self.rect.left >tela_largura/2+90:
            self.rect.left = tela_largura/2+90

class Fruta(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_fruta']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao de inicio
        self.rect.x = random.randint(tela_largura/2-2500, tela_largura/2+110)
        self.rect.y = random.randint(-200, -fruta_altura)
        #velocidade
        self.speedx = random.randint(x_fruta_min, x_fruta_max)
        self.speedy = random.randint(y_fruta_min,y_fruta_max)

    def update(self):
        # Posicao fruta
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < tela_largura/2-250 or self.rect.left >tela_largura/2+110:
            self.rect.x = random.randint(tela_largura/2-250, tela_largura/2+110)
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
        self.rect.x = random.randint(tela_largura/2-250, tela_largura/2+110)
        self.rect.y = random.randint(-200, -bota_altura)
        #velocidade
        self.speedx = random.randint(x_bota_min, x_bota_max)
        self.speedy = random.randint(y_bota_min, y_bota_max)

    def update(self):
        # posicao bota
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # limite tela
        if self.rect.top > tela_altura or self.rect.right < tela_largura/2-250 or self.rect.left >tela_largura/2+110:
            self.rect.x = random.randint(tela_largura/2-250, tela_largura/2+110)
            self.rect.y = random.randint(-200, -bota_altura)
            self.speedx = random.randint(x_bota_min, x_bota_max)
            self.speedy = random.randint(y_bota_min, y_bota_max)

def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    # Carrega o fundo
    fontcesta=pygame.font.SysFont(None,170)
    regra1=fontcesta.render('Pegue as frutas, não as botas!',True,(0,0,0))
    regra2=fontcesta.render('Aperte qualquer botão para começar!',True,(0,0,0))
    background = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
    background_rect = background.get_rect()
    jogando_i = True
    while jogando_i:
        #velocidade do jogo
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = fim
                jogando_i = False

            if event.type == pygame.KEYDOWN:
                condicao = jogo
                jogando_i = False

        tela.fill(preto)
        tela.blit(background, background_rect)
        pygame.display.flip()
        
    tela.blit(regra1,(300,400))
    tela.blit(regra2,(300,430))
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
    contador2=0
    # Botas
    for numero in range(numero_botas):
        bota = Bota(assets)
        sprites.add(bota)
        botas.add(bota)
    # Frutas
    for numero in range(numero_frutas):
        fruta = Fruta(assets)
        sprites.add(fruta)
        frutas.add(fruta)

    funcionando = True
    keys_down = {}

#loop
    while funcionando:
        clock.tick(FPS)
        if not frutas:
            funcionando = False
        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
                return 'repita',fim
            if funcionando:
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
        if encontros1:
            jogador.kill()
            keys_down = {}
            funcionando=False
            return 'repita',fim
        #verifica encontro entre cesta e frota
        encontros2 = pygame.sprite.spritecollide(jogador, frutas, True, pygame.sprite.collide_mask)
        if encontros2:
            contador2+=1
        if contador2> 3:
            keys_down = {}
            funcionando=False
            return 'continue',fim

        window.fill(preto) 
        window.blit(assets['background'], (tela_largura/2-350, 0))
        sprites.draw(window)
        pygame.display.update()  

def CESTA(window):
    pygame.init()
    pygame.display.set_caption('Cesta')

    #roda o jogo
    condicao = instrucao
    while condicao != fim:
        if condicao == instrucao:
            condicao = tela_de_instrucoes(window)
        elif condicao == jogo:
            resultado,condicao = tela_dentro_do_jogo(window)
            return resultado
        else:
            condicao = fim
    #encerra o jogo
