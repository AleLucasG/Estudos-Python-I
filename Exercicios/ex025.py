print()
print('Desafio 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.')
print()

nome = str(input('Seu nome tem “SILVA” no nome? Digite seu nome: ')).strip()
print(f'O nome contém "Silva"? {"SILVA" in nome.upper()}')
print(f'O nome contém "Silva"? {"silva" in nome.lower()}')
