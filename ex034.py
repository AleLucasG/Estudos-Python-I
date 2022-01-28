""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual valor do seu salario R$ '))
if salario <= 1249.99:
    aumento = (salario * 10)/ 100
    print('Seu aumento foi de 10% e seu salario atual é de R$ {:.2f}'.format(aumento+salario))
else:
    aumento = (salario * 15) /100
    print('Seu aumento foi de 15% e seu salario atual é de R$ {:.2f}'.format(aumento+salario))






