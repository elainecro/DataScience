# coding: iso-8859-1 -*-

#adaptado de https://redhuli.io/game-development/introduction-to-pygame/
# importando os m�dulos necess�rios
import pygame, sys
from pygame import *

#inicalizando o m�dlo pygame
pygame.init()

# Definindo as constantes  
window_width = 500   #comprimento da tela
window_height = 400   #altura da tela
FPS = 30 #definindo a taxa de atualiza��o da tela

black_color = (0,0,0)  #defini��o para a cor preta
white_color = (255,255,255)  #defini��o para a cor branca

#classe que representa um jogador
class Player(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        #chama o construtor para a classe Sprite
        super().__init__()

        # Cria o jogador (quadrado) com os valores passados
        self.image = pygame.Surface([width,height])
        self.image.fill(white_color)

        # Desenha o ret�ngulo na tela
        self.rect = self.image.get_rect()

        # Define as vari�veis do jogador
        self.changex = 0
        self.changey = 0

    def move_left(self, move_x):
        #movimenta para a esquerda
        self.changex -= move_x

    def move_right(self, move_x):
        #movimenta para a direita
        self.changex += move_x

    def gravity(self):
        #define a "gravidade"
        if self.changey == 0:
            self.changey = 0
        else:
            self.changey += .40

        if self.rect.bottom >= 360 and self.changey >= 0:
            self.changey = 0
            self.rect.y = 330
        
    def jump(self):
        #realiza o movimento de "pulo"
        if self.rect.bottom == 360: #altura m�xima do "pulo"
            self.changey = -10

    def update(self):
        #define a "gravidade"
        self.gravity()
        
        #atualiza o movimento do jogador
        self.rect.x += self.changex
        self.rect.y += self.changey

        #verifica se atingiu as bordas da imagem
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > window_width - self.rect.width:
            self.rect.x = window_width - self.rect.width

# define as taxas dos frames da tela
FPSCLOCK = pygame.time.Clock()

# define a tela que ser� utilizada
screen = pygame.display.set_mode((window_width, window_height))  #obt�m o objeto Surface
pygame.display.set_caption('Pygame - Jogo simples') #coloca o t�tulo da tela

# lista que cont�m todos os "blocos" do jogo
active_sprites_list = pygame.sprite.Group()
        
# Desenha o "bloco" nas posi��es indicadas
player = Player(30, 30)  #define o jogador(quadrado) de 30x30 pixels
player.rect.x = window_width / 2 - player.rect.centerx  #adiciona o ret�ngulo ao meio da tela (eixo x)
player.rect.y = 330  #desenha o "Jogador" na altura desejada

# Adiciona os blocos para a lista 
active_sprites_list.add(player)

#loop principal para o jogo
while True: 
    #recebe todos os eventos de intera��o com o jogo
    for event in pygame.event.get():
        
        #se clicar em sair da tela 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #recebe as teclas pessionadas
        if event.type == pygame.KEYDOWN:
            #tecla para a esquerda
            if event.key == pygame.K_LEFT:
                player.move_left(5)
            #tecla para a direita
            if event.key == pygame.K_RIGHT:
                player.move_right(5)
            #tecla para cima
            if event.key == pygame.K_UP:
                player.jump()
                
        
        #ao soltar a tecla
        if event.type == pygame.KEYUP:
            #atualiza ao soltar a tecla para a esquerda
            if event.key == pygame.K_LEFT:
                player.move_left(-5)
            #atualiza ao soltar a tecla para a direita
            if event.key == pygame.K_RIGHT:
                player.move_right(-5)

    # Adiciona a l�gica para o jogo
    active_sprites_list.update()

    # "desenha" o backgroud da tela 
    screen.fill(black_color)
        
    # desenha os "blocos" em cada momento de atualiza�ao
    active_sprites_list.draw(screen)

    pygame.display.update() # atualiza a tela
    FPSCLOCK.tick(FPS) # limita a taxa de atualiza��o da tela 