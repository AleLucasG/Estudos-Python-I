

# Se nenhum valor for digitado, o resultado é false
boleano = bool(input('Digite algo: '))
print(boleano)
print()

# Para verificar o tipo da variável (input retorna string)
n = input('Digite algo: ')
print(type(n))
print()

#  O tipo primitivo deve ser especificado para converter o valor
n1 = int(input('Digite algo: '))
print(type(n1))
print()

#Metodos de conversão
valor = input('Digite algo: ')
print(valor.isnumeric())
print(valor.isalpha())
