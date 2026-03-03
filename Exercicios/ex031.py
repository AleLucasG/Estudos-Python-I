print()
print('Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.\n'
      'Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
print()

distancia = float(input('Qual é a distancia da sua viajem em km? '))
preco1 = distancia * 0.50
preco2 = distancia * 0.45

if distancia <= 200:
    print(f'O percurso de {distancia} km, custara R$ {preco1:.2f}')
else:
    print(f'O percurso de {distancia} km, custara R$ {preco2:.2f}')
    
