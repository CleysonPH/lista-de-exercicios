# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

value_per_hour = float(input('Valor por hora: '))
hour_per_month = float(input('Horas por mês: '))

salary = value_per_hour * hour_per_month

print(f'O seu salario é {salary}')
