"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""

reta1 = float(input('1° tamanho: '))
reta2 = float(input('2° tamanho: '))
reta3 = float(input('3° tamanho: '))
triangulo = reta1 + reta2
if triangulo > reta3:
    print('\033[1;32mO comprimento das 3 retas PODEM FORMAR um triangulo \033[m \n')
else:
    print('\033[1;33mO comprimento das 3 retas NÂO PODE FORMAR um triangulo \033[m \n')

"""GUANABARA FEZ DA SUINTE FORMA"""
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;34mOs seguimentos acima PODEM formar tringulo \033[m')
else:
    print('\033[1;31mOs seguimentos acima NÃO PODEM formar triangulo \033[m')



