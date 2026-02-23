print()
print('Desafio 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, \n'
      'em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')
print()

frase = str(input('Digite uma frase: ')).strip().upper()
countA = frase.count('A')


print(f'Quantas vezes aparece a letra “A”: {countA}')
print(f'Em que posição ela aparece a primeira vez: {frase.find("A")} ')
print(f'Em que posição ela aparece a última vez: {frase.rfind("A")}')
