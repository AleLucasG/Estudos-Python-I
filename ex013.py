"""Faca um algoritmo que leia o salário de uma funcionário e mostre seu novo salári com aumento de 15%"""

salario = float(input('Digite seu salário atual R$ '))
novosal = salario + (salario * 15 / 100)
print('Salário atual é de R$ {:.2f} e com o aumento de 15% ficou em R$ {:.2f}'.format(salario, novosal))




