print()
print('15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. \n'
      'Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('')


km = float(input('Qual a quantidade de Km percorrido: '))
diasUso = int(input('Quantos dias que o carro foi alugado: '))
valorD= float(input('Valor diaria, carro alugado R$ '))
valorKm = float(input('Valor por km rodado R$ '))
print()

valorDias = diasUso * valorD
valorKm = km * valorKm
soma = valorDias + valorKm

print('====== DESCRITIVO ======')
print('O total de dias de uso R${:.2f}'.format(valorDias))
print('O total de Km percorridos R${:.2f}'.format(valorKm))
print('O carro foi alugado por {} dias e rodou {}km, total R${:.2f} a pagar.'.format(diasUso, km, soma))

