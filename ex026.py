"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez
- FRASE: ALESSANDRA LUCAS GOMES
- LETRA A: 4 VEZES
- POSIÇÃO: 1° - 0, e a 2° 14 (sem contar o espaço)"""

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A se repete {} x'.format(frase.count('A')))
print('A primeira posição da letra A é na posição: {}'.format(frase.find('A')))
print('A ultima posição da letra A é na posição: {}'.format(frase.rfind('A')))





