print()
print('Desafio  29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo \n'
      'que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')
print()

velocidade = int(input('Qual a velocidade que o carro estava? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado! Você ultrapassou a velocidade de 80Km/h.\n'
          f'Você vai receber uma multa de R$ {multa:.2f}.')
else:
    print('Você não utrapassou a velocidade de 80Km/h. Parabéns!')
