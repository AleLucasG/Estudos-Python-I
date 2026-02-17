print()
print('Desafio 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
print('A fórmula para converter Celsius para Fahrenheit é ºF = (ºC × 9/5) + 32, ou, de forma simplificada, ºF = (ºC × 1,8) + 32.')
print()

celsius = float(input('Qual a temperatura em graus Celsius: '))
fahrenheit1 = (celsius * 1.8) + 32
fahrenheit2 = (celsius * 9/5) + 32

print('A conversão {}°C em °F é de {}°F.'.format(celsius, fahrenheit1))
print('A conversão simplificada {}°C em °F é de {}°F.'.format(celsius, fahrenheit2))

