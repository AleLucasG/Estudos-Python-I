"""Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
Melhorando o código em: kilometros, ectometros, decametros, decimetros"""

n1 = float(input('Digite o valor de metros: '))
print('O valor de {:.2f} metros em centimetros é {} \nE em milimetros é de {} \n'.format(n1, n1*100, n1*1000))


"""Como Guanabara fez, usando duas variáveis: cm e mm"""

medida = float(input('Digite o valor de metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))




