print()
print('Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
print('Dados de 11/02/2026')
print()

real = float(input('Qual valor você tem disponível para conversão: R$ '))
dolar = real / 5.20
euro = real / 6.1873
pesosChile = real / 164.88
print('Com R${:.2f} você pode comprar U$${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar CLP{:.2f}'.format(real, pesosChile))