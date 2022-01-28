"""Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

PRECISA BAIXA UM ARQUIVO EM MP3

import pygame
pygame.init()
pygame.mixer.music.load('ex021.py')
pygame.mixer.music.play()
pygame.event.wait()

O pygame mudou de versão com isso precisei incluir um input ao código conforme abaixo:

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
"""

