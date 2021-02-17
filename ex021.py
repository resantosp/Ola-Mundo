import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('liga.mp3')
pygame.mixer.music.play(loops=3)
while(pygame.mixer.music.get_busy()): pass
