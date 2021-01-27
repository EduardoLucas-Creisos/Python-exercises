# carregue e reproduza um arquivo mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('NoOneLikeYou.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
