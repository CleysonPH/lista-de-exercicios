# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# Formula -> C = (5 * (F-32) / 9).

farenheit = float(input('Temperatura em Farenheit: '))

celsius = (5 * (farenheit-32) / 9)

print(f'{farenheit} graus em Farenheit é equivalente á {celsius} grau Celsius')
