print()
print('Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre: \n'
      '– O nome com todas as letras maiúsculas e minúsculas.\n'
      '– Quantas letras ao todo (sem considerar espaços).\n'
      '- Extra: Quantas letras tem o primeiro nome.')
print()

nome = str(input('Digite seu nome completo: ')).strip()
print(f'O nome com todas as letras maiúsculas: {nome.upper()}')
print(f'O nome com todas as letras minúsculas: {nome.lower()}')
print(f'Quantas letras ao todo: {len(nome) - nome.count(' ')} letras')
print(f'Quantas letras tem o primeiro nome: {nome.find(' ')} letras ')