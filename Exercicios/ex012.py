print()
print('Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
print()

preco = float(input('Informe o valor do produto R$  '))
desconto  = float(input('Informe o valor do desconto: '))
calculo1 = preco * (desconto / 100)
calculo2 = (preco * desconto) / 100
print()

print('Desconto de {}% em um produto de R${:.2f} é de R${:.2f}.'.format(desconto,preco, calculo1))
print('O produto que custava R${:.2f}, na promoção com desconto de %{}, vai custar R${:.2f}.'.format(preco,desconto, calculo2))