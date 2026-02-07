print()
print('Desafio 007: Desenvolva um programa que leia as duas notas de uma aluno, calcule e mostre a sua média.')
print()
nota1 = float(input('Primeiro valor: '))
nota2 = float(input('Segundo valor: '))
cal = (nota1 + nota2) / 2
print('A média do aluno é {}'.format(cal))
print('A média entre {:.1f} e {:.2f} é igual a {:.1f}' .format(nota1, nota2, (nota1+nota2)/2))