import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = int(input('Введите третье число: '))

y_1 = ((a ** 2 / 3) + (a ** 2 + 4) / b + math.sqrt(a ** 2 + 4) / 4 + math.sqrt(a ** 2 + 4) ** 3 / 4)
y_2 = ((math.cos(x ** 2) ** 2) + math.sin(2 ** x - 1) ** 2) ** 1 / 3
y_3 = math.cos(x) + math.sin(x)
y_4 = 5 * x + (3 * x) ** 2 * math.sqrt(1 + math.sin(x) ** 2)

print(y_1)
print(y_2)
print(y_3)
print(y_4)

#############################


i = int(input('Введите годовую процентную ставку: '))
s = int(input('Введите сумму займа: '))
n = int(input('Введите количество месяцев, на которые взят кредит: '))

p = i / s
m = (s * p * (1 + p) ** n) / ((1 + p) ** n - 1)

print(m)

#################################

R_1 = int(input('Введите радиус первой планеты: '))
R_2 = int(input('Введите радиус второй планеты: '))
V_1 = int(input('Введите скорость первой планеты : '))
V_2 = int(input('Введите скорость второй планеты : '))

L_1 = (2 * R_1 * math.pi) - V_1
L_2 = (2 * R_2 * math.pi) - V_2

raznitza = L_1 / L_2
print('Длина года первой планеты: ', L_1)
print('Длина года второй планеты: ', L_2)
print('Разница между первой и второй планетой: ', raznitza)
