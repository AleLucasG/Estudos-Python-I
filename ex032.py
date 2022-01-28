"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

print('===== TESTE 01 =====')
ano = int(input('Digite o ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('{} É ANO BISSEXTO \n'.format(ano))
else:
    print('{} NÃO É ANO BISSEXTO \n'.format(ano))

"""GUANABARA FEZ ASSIM"""
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É ANO BISSEXTO \n'.format(ano))
else:
    print('{} NÃO É ANO BISSEXTO \n'.format(ano))

"""O COMPUTADOR VAI IDENTIFICAR O ANO ATUAL DA MAQUINA"""

from datetime import date
ano = int(input('Coloque o n° 0 para analisar ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É ANO BISSEXTO \n'.format(ano))
else:
    print('{} NÃO É ANO BISSEXTO'.format(ano))



