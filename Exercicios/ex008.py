print()
print('Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros.')
print('Escala: km → hm → dam → M → dm → cm → mm')
print('Cada passo na escala vale 10 vezes.')
print('Descendo a escala → multiplica por 10')
print('Subindo a escala → divide por 10')

print()
metros = float(input('Digite um valor em metros: '))
centi = metros * 100
mili = metros * 1000
print('{} metros, é igual a {}cm e {}mm.'.format(metros, centi, mili))