import pygame
import random
import os

pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

tela_largura=400
tela_altura=600
FPS=60

background_largura=600
background_altura=450

pedra_largura=62
pedra_altura=109

papel_largura=62
papel_altura=109

tesoura_largura=62
tesoura_altura=109


instrucao = 0
jogo = 1
fim = 2


def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_jokenpo.jpg')).convert()
    assets['imag_pedra'] = pygame.image.load(os.path.join(pasta_img, 'Pedra.png')).convert_alpha()
    assets['imag_papel'] = pygame.image.load(os.path.join(pasta_img, 'Papel.png')).convert_alpha()
    assets['imag_tesoura'] = pygame.image.load(os.path.join(pasta_img, 'Tesoura.png')).convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], (background_largura, background_altura))
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
        self.rect.x = 100
        self.rect.y = 250

class Papel(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_papel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x =275
        self.rect.y =250

class Tesoura(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['imag_tesoura']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 250

def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    background = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
    background_rect = background.get_rect()
    jogando_i = True
    while jogando_i:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = fim
                jogando_i = False

            if event.type == pygame.KEYDOWN:
                condicao = jogo
                jogando_i = False

        tela.fill((0,0,0))
        tela.blit(background, background_rect)
        pygame.display.flip()

    return condicao

def tela_dentro_do_jogo(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    sprites = pygame.sprite.Group()
    pedras = pygame.sprite.Group()
    papeis = pygame.sprite.Group()
    tesouras = pygame.sprite.Group()

    groups = {}
    groups['sprites'] = sprites
    groups['pedras'] = pedras
    groups['papeis'] = papeis
    groups['tesouras'] = tesouras

    pedra= Pedra(assets)
    papel= Papel(assets)
    tesoura=Tesoura(assets)

    sprites.add(pedra)
    sprites.add(papel)
    sprites.add(tesoura)

    funcionando = True
    keys_down = {}

    while funcionando:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                print(x,y)
                if assets['imag_pedra'].get_rect().collidepoint(x,y):
                    funcionando = False
                    escolha_jogador='pedra'
                elif assets['imag_pedra'].get_rect().collidepoint(x,y):
                    escolha_jogador='papel'
                elif assets['imag_pedra'].get_rect().collidepoint(x,y):
                    escolha_jogador='tesoura'

                r=random.randint(1,3)
                if r==1:
                    escolha_bot='pedra'
                elif r==2:
                    escolha_bot='papel'
                else:
                    escolha_bot='tesoura'

                resultado='empate' 
                while resultado=='empate'
                    if escolha_jogador=='pedra' and escolha_bot=='pedra':
                        resultado='empate'
                    if escolha_jogador=='pedra' and escolha_bot=='papel':
                        resultado='bot'
                    if escolha_jogador=='pedra' and escolha_bot=='tesoura':
                        resultado='jogador'
                    if escolha_jogador=='papel' and escolha_bot=='papel':
                        resultado='empate'
                    if escolha_jogador=='papel' and escolha_bot=='tesoura':
                        resultado=''
                    if escolha_jogador=='tesoura' and escolha_bot=='tesoura':
                        resultado='empate'

        sprites.update()
        window.fill((0,0,0)) 
        window.blit(assets['background'], (0, 0))
        sprites.draw(window)
        pygame.display.update()  

#base
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((tela_altura, tela_largura))
pygame.display.set_caption('Jokenpo')

#roda o jogo
condicao = instrucao
while condicao != fim:
    if condicao == instrucao:
        condicao = tela_de_instrucoes(window)
    elif condicao == jogo:
        condicao = tela_dentro_do_jogo(window)
    else:
        condicao = fim
#encerra o jogo
pygame.quit()  