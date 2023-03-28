# Desafio 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. *módulos*
import pygame
pygame.init()
pygame.mixer.music.load('mrkrabs.mp3')
print('Parabéns!\nVocê agora está escutando maior obra prima já proporcionada a humanidade.')
pygame.mixer.music.play()
input()
pygame.event.wait()




