import pygame
import random
import os

pasta_img=os.path.join(os.path.dirname(__file__), 'imagens')

instrucao=0
jogo=1
fim=2

def tela_de_instrucoes(tela):
    background = pygame.image.load(os.path.join(pasta_img, 'imagem1.jpg')).convert()
    background_rect = background.get_rect()
    jogando = True
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condicao = instrucao
                jogando = False

            if event.type == pygame.KEYDOWN:
                condicao = jogo
                jogando = False

        tela.fill(0,0,0)
        tela.blit(background, background_rect)
        pygame.display.flip()

