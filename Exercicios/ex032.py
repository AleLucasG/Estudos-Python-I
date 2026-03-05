print()
print('Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('Formula: (Ano % 4 == 0 AND Ano % 100 != 0) OR (Ano % 400 == 0)')

import datetime

print('========= VERIFICANDO SE O ANO É BISSEXTO OU NÃO =========')
print()
ano = int(input('Digite o ano: '))

# Vericano o ano atual
#if ano == 0:
    #ano = datetime.date.today().year

if (ano % 4 == 0
        and ano % 100 != 0
        or ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} é NÃO É BISSEXTO.')