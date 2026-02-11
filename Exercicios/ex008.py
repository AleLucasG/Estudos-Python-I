print()
print('Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.')
print('Escala: km → hm → dam → m → dm → cm → mm')
print('Cada passo na escala vale 10 vezes.')
print('Descendo a escala → multiplica por 10')
print('Subindo a escala → divide por 10')
print()

metros = float(input('Digite um valor em metros: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000

dam = metros / 10
hm = metros / 100
km = metros / 1000

print('{} metros, é igual a {}dam, {}hm, {}km.'.format(metros, dam, hm, km))
print('{} metros, é igual a {}dm, {}cm, {}mm.'.format(metros, dm, cm, mm))

#com 2 casas decimais
print(f'{metros:.2f} m = {km:.2f} km, {hm:.2f} hm, {dam:.2f} dam')
print(f'{metros:.2f} m = {dm:.2f} dm, {cm:.2f} cm, {mm:.2f} mm')
