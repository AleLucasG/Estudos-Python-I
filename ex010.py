"""Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere - U$$ 1,00 = R$ 3,27"""

valor = float(input('Quanto você tem na carteira R$ '))
dolar = valor / 3.27
print('Com R$ {:.2f} reais, você pode comprar U$$ {:.2f} dolares' .format(valor, dolar))







