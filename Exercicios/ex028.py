print()
print('Desafio 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça \n'
      'para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.')
print()

import random
#from random import randint
import time

usuario = int(input('Digite um número inteiro entre 0 e 5: '))
maquina = random.randint(0,5)

print('Processando...')
time.sleep(2)
print('Processando.....')
time.sleep(2)
print('Processando........')
print()
if usuario == maquina:
    print('Você acertou o número escolhido! Parabéns!!!')
else:
    print('Você errou!\n'
          f'O número escolhido foi: {maquina}, e você digitou: {usuario}.')
