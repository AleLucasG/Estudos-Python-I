"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = float(input('Qual a velocidade do carro: '))
if velocidade <= 80:
    print('\033[4;32mVOCÊ ESTA NA VELOIDADE MEDIA, PROSSIGA!')
else:
    print('\033[1;31mVOCÊ ESTA DIRIGINDO ACIMA DA VELOCIDADE E SERA MULTADO')
    multa = (velocidade - 80) * 7.00
    print("\033[1;31mSua multa é de R$ {:.2f}".format(multa))




