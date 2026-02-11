print()
print('Desafio 007: Desenvolva um programa que leia as duas notas de uma aluno, calcule e mostre a sua média.')
print()
nota1 = float(input('Primeiro nota: '))
nota2 = float(input('Segundo nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno é {}'.format(media))
print('A média entre as notas {:.1f} e {:.2f} é igual a {:.1f}' .format(nota1, nota2, (nota1+nota2)/2))