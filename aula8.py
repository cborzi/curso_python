import datetime

nome = 'Carlos'
idade = 54
altura = 1.78
peso = 82
imc = peso / (altura ** 2)
nascimento = datetime.date.today().year - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

num_1 = 2
num_2 = 2.2
num_3 = num_1 + num_2
num_4 = 'c' + 'a'
print(num_3)
print(num_4)


