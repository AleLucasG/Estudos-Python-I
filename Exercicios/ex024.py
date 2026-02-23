print()
print('Desafio 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.')
print()

nome = str(input('Digite o nome do cidade: ')).strip()
print(f'A cidade começa com "Santo"? {nome[:5].upper() == "SANTO"}')
print(f'A cidade começa com "Santo"? {nome.upper().startswith("SANTO")}')
