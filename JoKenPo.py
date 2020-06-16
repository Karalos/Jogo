#imports
import pygame
import random
import os
################veceu eh a variavel que pode ser usada para confirmar a vitoria do jogo#################################
#origem das imagens
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')
pasta_font=os.path.join(os.path.dirname(__file__), 'fontes')

#parametros
tela_largura=1100
tela_altura=600
FPS=60

background_largura=1100
background_altura=600

pedra_largura=100
pedra_altura=175

papel_largura=100
papel_altura=175

tesoura_largura=100
tesoura_altura=175

#"fases" do jogo
instrucao = 0
jogo = 1
fim = 2
#vitorias
melhor_de=3

#tempo
tempo_de_amostra=3000 #milisegundos

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
    assets["fonte_texto"] = pygame.font.Font(os.path.join(pasta_font, 'Destacy.ttf'), 80)
    assets['fonte_texto2']=pygame.font.Font(os.path.join(pasta_font, 'PressStart2P.ttf'),65)
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
        self.rect.x = 170
        self.rect.y = 370

class Papel(pygame.sprite.Sprite):
    #codigo base
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        self.image = assets['imag_papel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao do objeto
        self.rect.x =470
        self.rect.y =370

class Tesoura(pygame.sprite.Sprite):
    #codigo base
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        self.image = assets['imag_tesoura']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #posicao do objeto        
        self.rect.x = 770
        self.rect.y = 370

#funcao utilizada para definir quem é o vencedor
def funcao_resultado(escolha_jogador,escolha_bot):
    if escolha_jogador=='pedra' and escolha_bot=='pedra':
        return 'Empatou'
    if escolha_jogador=='pedra' and escolha_bot=='papel':
        return 'Voce perdeu'
    if escolha_jogador=='pedra' and escolha_bot=='tesoura':
        return 'Voce venceu'
    if escolha_jogador=='papel' and escolha_bot=='pedra':
        return 'Voce venceu'
    if escolha_jogador=='papel' and escolha_bot=='papel':
        return 'Empatou'
    if escolha_jogador=='papel' and escolha_bot=='tesoura':
        return 'Voce perdeu'
    if escolha_jogador=='tesoura' and escolha_bot=='pedra':
        return 'Voce perdeu'
    if escolha_jogador=='tesoura' and escolha_bot=='papel':
        return 'Voce venceu'
    if escolha_jogador=='tesoura' and escolha_bot=='tesoura':
        return 'Empatou'

#telas do jogo
def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    #imagem
    background = pygame.transform.scale(pygame.image.load(os.path.join(pasta_img, 'Jokenpo.png')).convert(),(1000,600))
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

    #placar
    placar_player=0
    placar_bot=0

    #codigo jogo
    funcionando = True
    while funcionando:
        clock.tick(FPS)
        #eventos
        for event in pygame.event.get():
            #fechar jogo
            if event.type == pygame.QUIT:
                funcionando = False
                return ['repita',fim]
            #verificar clique
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.get_blocked(pygame.MOUSEBUTTONDOWN)
                #dados do mouse
                posicao_mouse=event.pos
                #variavel que determina se o jogador escolheu uma das opcoes disponiveis
                escolha=True
                #comparar dodos do mouse com sprites
                sprites_selecionados = [s for s in sprites if s.rect.collidepoint(posicao_mouse)]
                #verificar escolha do jogador
                if sprites_selecionados in pedras:
                    escolha_jogador='pedra'
                elif sprites_selecionados in papeis:
                    escolha_jogador='papel'
                elif sprites_selecionados in tesouras:
                    escolha_jogador='tesoura'
                else:
                    escolha=False
                #verifica se a escolha do jogador foi aceitavel
                if escolha: 
                    #define a escolha do bot              
                    r=random.randint(1,3) #cada clique gera um novo r   
                    if r==1:
                        escolha_bot='pedra'
                        imag_escolha_op=assets['imag_pedra']
                    if r==2:
                        escolha_bot='papel'
                        imag_escolha_op=assets['imag_papel']
                    if r==3:
                        escolha_bot='tesoura'
                        imag_escolha_op=assets['imag_tesoura']
                    #verificar o resultado
                    resposta=funcao_resultado(escolha_jogador,escolha_bot)
                    #define resposta 
                    texto = assets['fonte_texto'].render(resposta, True, (255,255,255))
                    #area da resposta 
                    local_texto = texto.get_rect()
                    local_texto.midtop = (background_largura / 2 -40,  20)
                    #sprite da escolha do oponente
                    imag_escolha_op=pygame.transform.rotate(imag_escolha_op, 180)
                    local_imag_op=imag_escolha_op.get_rect()
                    local_imag_op.midtop=(background_largura/2 -40, 140)
                    window.blit(imag_escolha_op,local_imag_op)
                    pygame.display.flip
                    #apresenta textos
                    window.blit(texto, local_texto)
                    pygame.display.update()  
                    #tempo para ler a resposta
                    pygame.event.clear()
                    pygame.time.wait(tempo_de_amostra)
                    pygame.event.clear()
                    if resposta=='Empatou':
                        pass
                    elif resposta== 'Voce venceu':
                        placar_player+=1
                    elif resposta== 'Voce perdeu':
                        placar_bot+=1      
                    if placar_bot==(melhor_de):
                        return ['repita',fim]
                        funcionando=False
                    elif placar_player==(melhor_de):
                        return ['continue',fim]
                        funcionando=False


        #background
        window.fill((0,0,0)) 
        window.blit(assets['background'], (0, 0))
        #placar bot
            #dono da pontuacao
        nome_placar_b = assets['fonte_texto'].render('oponente', True, (255,255,255))     
        local_nome_placar_b=nome_placar_b.get_rect()
        local_nome_placar_b.midtop=(background_largura-240,-50)
        window.blit(nome_placar_b, local_nome_placar_b)            
            #pontuacao
        placar_b = assets['fonte_texto2'].render("{:02d}".format(placar_bot), True, (255,255,0))     
        local_placar_b=placar_b.get_rect()
        local_placar_b.midtop=(background_largura-240,110)
        window.blit(placar_b, local_placar_b)
        #placar player
            #dono da pontuacao
        nome_placar_p = assets['fonte_texto'].render('jogador', True, (255,255,255))     
        local_nome_placar_p=nome_placar_p.get_rect()
        local_nome_placar_p.midtop=(130,-50)
        window.blit(nome_placar_p, local_nome_placar_p)                
            #pontuacao
        placar_p= assets['fonte_texto2'].render("{:02d}".format(placar_player), True, (255,255,0))   
        local_placar_p=placar_p.get_rect()
        local_placar_p.midtop=(120,110)
        window.blit(placar_p, local_placar_p)   
        #update

        sprites.draw(window)
        sprites.update()
        pygame.display.update()  



def JOKENPO(window):
    #pygame.init()
    #pygame.mixer.init()
    pygame.display.set_caption('Jokenpo')
    #roda o jogo
    condicao = instrucao
    while condicao != fim:
        if condicao == instrucao:
            condicao = tela_de_instrucoes(window)
        elif condicao == jogo:
            res = tela_dentro_do_jogo(window)
            resultado=res[0]
            condicao=res[1]
            return resultado
        else:
            condicao = fim
