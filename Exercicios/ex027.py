print()
print('Desafio 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')
print()

nome = str(input('Digite seu nome completo: ')).strip()
separar = nome.split()
print(f'Primeiro nome: {separar[0]}')
print(f'Segundo nome: {separar[len(separar)-1]}')
