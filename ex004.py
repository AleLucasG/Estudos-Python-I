"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele"""

valor = input('Digite algo: ')
print('Tipo primitivo é:', type(valor))
print('É alfabético:', valor.isalpha())
print('É alfanumérico:', valor.isalnum())
print('É um número:', valor.isnumeric())
print('É um numero decimal:', valor.isdecimal())
print('Esta em letras maiúsculas:', valor.isupper())
print('Esta em letras minúsculas:', valor.islower())
print('Esta capitalizada:', valor.istitle())





