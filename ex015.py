"""Escreva uma programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por km rodado"""

print('=====1° TESTE====')
dias = int(input('Quantos dias alugado: '))
valordias = dias * 60.00

km = float(input('Quantos km rodados: '))
valorkm = km * 0.15

print('Total a pagar é de R${:.2f} \n'.format(valordias + valorkm))


print('====2° TESTE====')
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos km rodados: '))
total = (dias * 60.00) + (km * 0.15)
print('Total a pagar é de R${:.2f}'.format(total))

