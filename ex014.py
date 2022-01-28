"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit"""

c = float(input('Informe a temperatura em °C: '))
f = 32 + (c * 1.8)
print('A temperatura de {:.1f}°C corresponde a {}°F'.format(c, f))

