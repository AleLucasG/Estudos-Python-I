# Print do = 20x
print('=' * 20)
print()

nome = input('Qual é seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))

# imprime o nome ocupando 20 espaços
print('Prazer em te conhecer {:20}!'.format(nome))

# alinhamento à direita
print('Prazer em te conhecer {:>20}!'.format(nome))

# alinhamento à esquerda (a exclamação fica no final)
print('Prazer em te conhecer {:<20}!'.format(nome))

# centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))

# centralizado, preenchendo com '='
print('Prazer em te conhecer {:=^20}!'.format(nome))

n2 = int(input('Digite valor1: '))
n3 = int(input('Digite valor2: '))
soma = n2 + n3
sub = n2 - n3
mult = n2 * n3
div = n2 / n3
potencia = n2 ** n3
divisaointeira = n2 // n3
rest = n2 % n3
print('Resultados: soma: {}, subtração: {}, multiplição: {} e divisão: {}'.format(soma, sub, mult, div), end=' ')
print('potencia: {}, divisao inteira {}, resto da divisão {}'.format(potencia, divisaointeira, rest))
