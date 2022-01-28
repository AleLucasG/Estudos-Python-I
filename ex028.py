"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
ou perdeu."""

from random import randint

print('       ===== TESTE 01 =====')
print('\033[1;34m == ESCOLHA UM NÚMERO DE 0 A 5 == \033[m \n')

computador = randint(0, 5)
num = int(input('Qual número de 0 a 5 você escolheu: '))
print('O computador escolheu: {}'.format(computador))
if num == computador:
    print('\033[1;30mPARABENS, VOCÊ ACERTOU! \033[m')
else:
    print('\033[1;33mVOCÊ ERROU! TENTE NOVAMENTE! \033[m\n')

from random import choice

print('       ===== TESTE 02 =====')
print('\033[35m == ESCOLHA UM NÚMERO DE 0 A 10 == \033[m \n')

num = [0,1,2,3,4,5,6,7,8,9,10]
computador = choice(num)
num = int(input('Qual número você escolheu: '))
print('O computador escolheu o número: {}'.format(computador))
if num == computador:
    print('\033[1;35mMEUS PARABÉNS, VOCÊ ACERTOU! \033[m')
else:
    print('\033[1;36mMELHOR SORTE NA PROXIMA TENTATIVA! \033[m')






