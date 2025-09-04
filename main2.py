import pygame
import os

#nicializando o Pygame
pygame.init()

#Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coca-Collastic Game com imágem.")

#definindo cor de fundo
BG_COLOR = (142, 171, 245) #cor de fundo, azul-goiaba

#carregar imagem
image_file = "imagem-colla.png" #nome da imagem
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() #carrega imagem
    img_react = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # centraliza a imagem
else:
    print("Imágem não encontrada")

#loop princial do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #preencher o fundo
    screen.fill(BG_COLOR)

    #desenhar a imagem na tela
    screen.blit(img, img_react.topleft)

    #atualizar a tela
    pygame.display.flip()

#finalizar o pygame
pygame.quit()