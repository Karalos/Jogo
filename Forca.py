import pygame
import random
import os
import time
import threading

cor=(255,255,255)

#origem das imagens
pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')
pasta_font=os.path.join(os.path.dirname(__file__), 'fontes')
###################################################################################
#parametros
tela_largura=1100
tela_altura=600
FPS=60

background_largura=1100
background_altura=600
#################################################################################
'FORCA'
#forca vertical
forca_v_coordenadas=(30,160,20,300)
#forca horizontal
forca_h_coordenadas=(10,180,200,20)
#forca corda
forca_corda_coordenadas=(145,180,10,50)

'STICKMAN'
#cabeca
cabeca_raio=35
cabeca_espessura=10
cabeca_coordenadas=(150,250)
#corpo
corpo_coordenadas=(145,275,10,100)
#braco_esquerdo
braco_esquerdo_coordenadas=((145,280),(145,290),(95,320),(95,310))
#braco_direito
braco_direito_corcoordenadas=((155,280),(155,290),(215,320),(215,310))
#perna_esquerda
perna_esquerda_coordenadas=((145,375),(145,355),(95,465),(105,465))
#perna_direita
perna_direita_corcoordenadas=((155,375),(155,355),(205,465),(195,465))

'CAIXA DE TEXTO ERROS'
texto_erros_coordenadas=(530,170)
caixa_texto_coordenadas_h_1=(450,220,260,5)
caixa_texto_coordenadas_h_2=(450,290,260,5)
caixa_texto_coordenadas_v_1=(450,220,5,70)
caixa_texto_coordenadas_v_2=(710,220,5,75)

'chao dos acertos'
chao_texto_1_coordenadas=(350,360,60,10)
chao_texto_2_coordenadas=(450,360,60,10)
chao_texto_3_coordenadas=(550,360,60,10)
chao_texto_4_coordenadas=(650,360,60,10)
chao_texto_5_coordenadas=(750,360,60,10)

#palavra certa
palavra_certa_coordenadas=(550,400)
###################################################################################
#"fases" do jogo
instrucao = 0
jogo = 1
fim = 2

#inicia jogo
pygame.init()

#cria tela
window = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('Forca')


######################################################################################
#palavra escolhida
lista_palavra_escolhida=['sagaz','mexer','termo','senso','nobre','pleno','afeto','audaz','sutil','inato','desde','vigor','sanar','fazer','ideia','anexo','poder','justo','moral','honra','lapso','muito','expor','posse','prole','digno','haver','pesar','tenaz','genro','atroz','dizer','causa','denso','ceder','brado','dever','comum','censo','sobre','culto','saber','fugaz','casal','tempo','louco','sendo','manso','mundo','sonho']
palavra_escolhida=lista_palavra_escolhida[random.randint(1,50)]
######################################################################################
#carregando imagens
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(pasta_img, 'fundo_jokenpo.jpg')).convert()
    assets['background'] = pygame.transform.scale(assets['background'], (background_largura, background_altura))
    assets["fonte_texto"] = pygame.font.Font(os.path.join(pasta_font, 'Overlock-Black.ttf'), 40)
    return assets

############################################################################################  
#########################################################################
def tela_de_instrucoes(tela):
    clock = pygame.time.Clock()
    #imagem
    tela_instr = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
    tela_instr_rect = tela_instr.get_rect()
    fontforca=pygame.font.SysFont(None,70)
    regra1=fontforca.render('Advinhe a palavra;',True,(0,0,0))
    regra2=fontforca.render('Você terá 8 chances;',True,(0,0,0))
    regra3=fontforca.render('Aperte qualquer botão para começar o jogo', True,(0,0,0))
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
                
        tela.blit(regra1,(100,400))
        tela.blit(regra2,(100,440))
        tela.blit(regra3,(100,480))
        tela.fill(cor)
        tela.blit(tela_instr, tela_instr_rect)
        pygame.display.flip()
    return condicao

########################################################################################
def tela_dentro_do_jogo(window):
    #listas
    lista_chutes=[]
    lista_erros=[]
    lista_acertos=[]
    erros=0
    clock = pygame.time.Clock()
    #carregar imagens
    assets = load_assets()
    #loop   
    game = True
    while game:
        clock.tick(FPS)
        #verifica eventos
        for event in pygame.event.get():
            #encerra jogo
            if event.type == pygame.QUIT:
                return 'repita',fim
                game = False
            #evento teste
            chute='pass'
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    chute='a'
                if event.key==pygame.K_b:
                    chute='b'
                if event.key==pygame.K_c:
                    chute='c'
                if event.key==pygame.K_d:
                    chute='d'
                if event.key==pygame.K_e:
                    chute='e'
                if event.key==pygame.K_f:
                    chute='f'
                if event.key==pygame.K_g:
                    chute='g'
                if event.key==pygame.K_h:
                    chute='h'
                if event.key==pygame.K_i:
                    chute='i'
                if event.key==pygame.K_j:
                    chute='j'
                if event.key==pygame.K_k:
                    chute='k'
                if event.key==pygame.K_l:
                    chute='l'
                if event.key==pygame.K_m:
                    chute='m'
                if event.key==pygame.K_n:
                    chute='n'
                if event.key==pygame.K_o:
                    chute='o'
                if event.key==pygame.K_p:
                    chute='p'
                if event.key==pygame.K_q:
                    chute='q'
                if event.key==pygame.K_r:
                    chute='r'
                if event.key==pygame.K_s:
                    chute='s'
                if event.key==pygame.K_t:
                    chute='t'
                if event.key==pygame.K_u:
                    chute='u'
                if event.key==pygame.K_v:
                    chute='v'
                if event.key==pygame.K_w:
                    chute='w'
                if event.key==pygame.K_x:
                    chute='x'
                if event.key==pygame.K_y:
                    chute='y'
                if event.key==pygame.K_z:
                    chute='z'
                #verifica tecla
                #verifica se o caractere digitado foi uma letra
                if chute!='pass':
                    #verifica se o caractere ja foi utilizado
                    if chute not in lista_chutes :
                        #adiciona o caractere à lista de usados
                        lista_chutes.append(chute)
                        #verifica se ele esta ou nao na palavra escolhida
                        if chute in palavra_escolhida:
                            lista_acertos.append(chute)
                            #se foi erro ou nao
                            verifica_tecla= 0
                        if chute not in palavra_escolhida:
                            lista_erros.append(chute)
                            #se foi erro ou nao                
                            verifica_tecla= 1 
                    else:
                        #se foi erro ou nao   
                        verifica_tecla= 0
                else:
                    #se foi erro ou nao
                    verifica_tecla= 0        
                erros+=verifica_tecla
        #tela de fundo
        window.fill((255,255,0))
        window.blit(assets['background'], (0, 0)) 

        #desenha stickman/forca e verifica derrota
        if erros>0:
            pygame.draw.rect(window,cor,forca_h_coordenadas)
        if erros>1:
            pygame.draw.rect(window,cor,forca_v_coordenadas)

        if erros>2:
            pygame.draw.rect(window,cor,forca_corda_coordenadas)
            pygame.draw.circle(window,cor,cabeca_coordenadas,cabeca_raio,cabeca_espessura)

        if erros >3:
            pygame.draw.rect(window,cor,corpo_coordenadas)

        if erros >4:
            pygame.draw.polygon(window,cor,braco_esquerdo_coordenadas)

        if erros >5:
            pygame.draw.polygon(window,cor,braco_direito_corcoordenadas)

        if erros >6:
            pygame.draw.polygon(window,cor,perna_esquerda_coordenadas)

        if erros >7:  
            pygame.draw.polygon(window,cor,perna_direita_corcoordenadas)
            #desenha a palavra certa
            palavra_certa = assets['fonte_texto'].render(palavra_escolhida, True, (cor))     
            local_palavra_certa=palavra_certa.get_rect()
            local_palavra_certa.midtop=(palavra_certa_coordenadas)
            window.blit(palavra_certa, local_palavra_certa)
            game=False
            return 'repita',fim

        # verifica vitoria
        i=0
        for letra in palavra_escolhida:
            if letra in lista_acertos:
                i+=1
        if i==5:
            return 'continue',fim
            game = False

        #desenha quadrado onde estarao os erros e os erros
            #palavra :'Erros'
        letras_erro = assets['fonte_texto'].render("Erros", True, (cor))     
        local_letras_erro=letras_erro.get_rect()
        local_letras_erro.midtop=(texto_erros_coordenadas)
        window.blit(letras_erro, local_letras_erro)
            #Rretangulo erros
        pygame.draw.rect(window,cor,caixa_texto_coordenadas_h_1)
        pygame.draw.rect(window,cor,caixa_texto_coordenadas_h_2)
        pygame.draw.rect(window,cor,caixa_texto_coordenadas_v_1)
        pygame.draw.rect(window,cor,caixa_texto_coordenadas_v_2)
            #Desenha erros
        letras_erradas_x=445
        letras_erradas_y=230
        if len(lista_erros) <=8:
            for letra in lista_erros:
                #muda posicao letras
                letras_erradas_x+=30
                #desenha letras
                letras_erradas = assets['fonte_texto'].render(letra, True, (cor))     
                local_letras_erradas=letras_erradas.get_rect()
                local_letras_erradas.midtop=(letras_erradas_x,letras_erradas_y)
                window.blit(letras_erradas, local_letras_erradas)

        #desenha quadrados onde estarao os acertos
            #desenha chao
        pygame.draw.rect(window,cor,chao_texto_1_coordenadas)
        pygame.draw.rect(window,cor,chao_texto_2_coordenadas)
        pygame.draw.rect(window,cor,chao_texto_3_coordenadas)
        pygame.draw.rect(window,cor,chao_texto_4_coordenadas)
        pygame.draw.rect(window,cor,chao_texto_5_coordenadas)
            #desenha letras
        dicio_posicaosicoes={}
        for letras in lista_acertos:
            posicoes=[pos for pos, simbolo in enumerate(palavra_escolhida) if simbolo == letras]
            dicio_posicaosicoes.update({letras:posicoes})
            for chaves,valores in dicio_posicaosicoes.items():
                for elemento in valores:
                    if elemento==0:
                        letra_colocar = assets['fonte_texto'].render(chaves, True, (cor))     
                        local_letra_colocar=letra_colocar.get_rect()
                        local_letra_colocar.midtop=(380,310)
                        window.blit(letra_colocar, local_letra_colocar)

                    if elemento==1:
                        letra_colocar = assets['fonte_texto'].render(chaves, True, (cor))     
                        local_letra_colocar=letra_colocar.get_rect()
                        local_letra_colocar.midtop=(480,310)
                        window.blit(letra_colocar, local_letra_colocar)

                    if elemento==2:
                        letra_colocar = assets['fonte_texto'].render(chaves, True, (cor))     
                        local_letra_colocar=letra_colocar.get_rect()
                        local_letra_colocar.midtop=(580,310)
                        window.blit(letra_colocar, local_letra_colocar)

                    if elemento==3:
                        letra_colocar = assets['fonte_texto'].render(chaves, True, (cor))     
                        local_letra_colocar=letra_colocar.get_rect()
                        local_letra_colocar.midtop=(680,310)
                        window.blit(letra_colocar, local_letra_colocar)
                    if elemento==4:
                        letra_colocar = assets['fonte_texto'].render(chaves, True, (cor))     
                        local_letra_colocar=letra_colocar.get_rect()
                        local_letra_colocar.midtop=(780,310)
                        window.blit(letra_colocar, local_letra_colocar)
        #atualiza desenhos
        pygame.display.update()
    #encerra jogos
    pygame.quit()  
  ############################################################################  
def FORCA(WINDOW): 
    #roda o jogo
    pygame.init()
    pygame.display.set_caption('Forca')
    condicao = instrucao
    while condicao != fim:
        if condicao == instrucao:
            condicao = tela_de_instrucoes(window)
        elif condicao == jogo:
            resposta,condicao = tela_dentro_do_jogo(window)
            return resposta
        else:
            condicao = fim
    #encerra o jogo
