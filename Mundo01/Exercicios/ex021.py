import pygame

pygame.init()

pygame.mixer.music.load("../Outros/umib_020.ogg")
pygame.mixer.music.play()
input()
pygame.event.wait()
