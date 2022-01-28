"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""

preço = float(input('Qual o preço do produto R$ '))
desconto = preço - ( preço * 5 / 100)
print('O produto custa R$ {:.2f}. Com desconto de 5%, custara R$ {:.2f}.'.format(preço, desconto))










