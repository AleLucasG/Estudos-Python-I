#CONDIÇÕES: Ou uma, ou outra condição sera executada.
print()
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 5:
    print('Carro novo')
else:
    print('Carro velho')
print('========= FIM =========')

#outra forma
print('Carro novo' if tempo <= 5 else 'Carro velho')
print('========= FIM =========')
print()

#
nome = str(input('Qual o seu nome? '))
if nome == 'Alessandra':
    print('Que belo nome!')
else:
    print('Seu nome é comum.')
print(f'Bom dia dia {nome}')
print()

#
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua media foi: {media}')

if media >= 7.0:
    print('Sua media foi boa!')
else:
    print('Sua media foi ruim!')
# ou
print('Parabéns' if media >=7 else 'Estude mais!')