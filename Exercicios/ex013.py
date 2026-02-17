print()
print('Desafio 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
print()

salarioAtual = float(input('Informe seu salário atual R$ '))
pencentual = float(input('Informe o percentual de aumento: '))
aumento = (salarioAtual * pencentual) / 100
total = aumento + salarioAtual
print()

print('Seu salário de R${}, teve um reajuste {}%.'.format(salarioAtual, pencentual))
print('{}% sobre o salário de R${}, é igual a R${} de aumento.'.format(pencentual, salarioAtual, aumento))
print('Seu salário agora passa a ser R$ {:,.2f} ao final do més.'.format(total).replace(',', 'X').replace('.', ',').replace('X', '.'))


