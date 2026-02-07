print('Testando formas de impressão')

nome = 'Alessandra'
idade = 28
print(type(idade))

print('Meu nome é',nome, 'e tenho',idade, 'anos')
print('Meu nome é {} e tenho {} anos'.format(nome, idade))
print('Tenho {0} anos e me chamo {1}'.format(28, 'Alessandra'))
print(f'Meu nome é {nome} e tenho {idade} anos')
print()

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
print('A soma entre {0} e {1} é igual a: {2}'.format(n1, n2, soma))
