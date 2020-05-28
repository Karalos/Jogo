#imports
import pygame
import random
import os

#origem das imagens
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

#parametros
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

#"fases" do jogo
instrucao = 0
jogo = 1
fim = 2

#carregando imagens
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
#classes
class Pedra(pygame.sprite.Sprite):
    #codigo base
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        self.image = assets['imag_pedra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao do objeto
        self.rect.x = 100
        self.rect.y = 250

class Papel(pygame.sprite.Sprite):
    #codigo base
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        self.image = assets['imag_papel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao do objeto
        self.rect.x =275
        self.rect.y =250

class Tesoura(pygame.sprite.Sprite):
    #codigo base
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        self.image = assets['imag_tesoura']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao do objeto        
        self.rect.x = 450
        self.rect.y = 250

#funcao utilizada para definir quem é o vencedor
def funcao_resultado(escolha_jogador,escolha_bot):
    if escolha_jogador=='pedra' and escolha_bot=='pedra':
        return 'empate'
    if escolha_jogador=='pedra' and escolha_bot=='papel':
        return 'bot'
    if escolha_jogador=='pedra' and escolha_bot=='tesoura':
        return 'jogador'
    if escolha_jogador=='papel' and escolha_bot=='pedra':
        return 'jogador'
    if escolha_jogador=='papel' and escolha_bot=='papel':
        return 'empate'
    if escolha_jogador=='papel' and escolha_bot=='tesoura':
        return 'bot'
    if escolha_jogador=='tesoura' and escolha_bot=='pedra':
        return 'bot'
    if escolha_jogador=='tesoura' and escolha_bot=='papel':
        return 'jogador'
    if escolha_jogador=='tesoura' and escolha_bot=='tesoura':
        return 'empate'

#telas do jogo
def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    #imagem
    background = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
    background_rect = background.get_rect()
    #codigo jogo
    jogando_i = True
    while jogando_i:
        clock.tick(FPS)
        #eventos
        for event in pygame.event.get():
            #fechar o jogo
            if event.type == pygame.QUIT:
                condicao = fim
                jogando_i = False
            #ir para proxima fase
            if event.type == pygame.KEYDOWN:
                condicao = jogo
                jogando_i = False

        tela.fill((0,0,0))
        tela.blit(background, background_rect)
        pygame.display.flip()
    return condicao


def tela_dentro_do_jogo(window):
    clock = pygame.time.Clock()

    #carregar imagens
    assets = load_assets()
    sprites = pygame.sprite.Group()
    pedras = pygame.sprite.Group()
    papeis = pygame.sprite.Group()
    tesouras = pygame.sprite.Group()

    #criar grupos
    groups = {}
    groups['sprites'] = sprites
    groups['pedras'] = pedras
    groups['papeis'] = papeis
    groups['tesouras'] = tesouras

    #definir possiveis 'participantes'
    pedra= Pedra(assets)
    papel= Papel(assets)
    tesoura=Tesoura(assets)

    #preencher grupos
    sprites.add(pedra)
    sprites.add(papel)
    sprites.add(tesoura)
    pedras.add(pedra)
    papeis.add(papel)
    tesouras.add(tesoura)

    #codigo jogo
    funcionando = True
    while funcionando:
        clock.tick(FPS)
        #eventos
        for event in pygame.event.get():
            #fechar jogo
            if event.type == pygame.QUIT:
                funcionando = False
            #verificar clique
            if event.type == pygame.MOUSEBUTTONDOWN:
                #dados do mouse
                posicao_mouse=event.pos
                #comparar dodos do mouse com sprites
                sprites_selecionados = [s for s in sprites if s.rect.collidepoint(posicao_mouse)]
                #verificar escolha do jogador
                if sprites_selecionados in pedras:
                    print('pedra')
                    escolha_jogador='pedra'
                elif sprites_selecionados in papeis:
                    escolha_jogador='papel'
                    print('papel')
                elif sprites_selecionados in tesouras:
                    escolha_jogador='tesoura'
                    print('tesoura') 
                #definir escolha do bot               
                r=random.randint(1,3) #cada clique gera um novo r   
                if r==1:
                    escolha_bot='pedra'
                    print('pedra')
                elif r==2:
                    escolha_bot='papel'
                    print('papel')
                else:
                    escolha_bot='tesoura'
                    print('tesoura')
                #verificar resposta
                resposta=funcao_resultado(escolha_jogador,escolha_bot)
                print(resposta)

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