"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média"""

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
print('A média entre {:.1f} e {:.2f} é igual a {:.1f}' .format(n1, n2, (n1+n2)/2))
