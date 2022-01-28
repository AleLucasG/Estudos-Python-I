"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

num = str(input('Digite um número: '))
x = [int(a) for a in str(num)]
print(x, '\n')

""" O Número num é primeiro convertido em uma string usando str() no código acima. Em seguida, é usada a compreensão de 
lista, que divide a string em dígitos discretos. Finalmente, os dígitos são convertidos de volta para um inteiro
 usando a função int()."""

"""COMO O PROF. GUANABARA FEZ"""

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

"""O símbolo // faz a divisão e so pega o que esta antes da vírgula
O símbolo % faz a divisão e só pega o que estav depois da vírgula"""


