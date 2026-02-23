print()
print('Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre: \n'
      '– O nome com todas as letras maiúsculas e minúsculas.\n'
      '– Quantas letras ao todo (sem considerar espaços).')
print()

nome = str(input('Digite seu nome completo: '))
print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(f'{len(nome) - nome.count(' ')} letras')