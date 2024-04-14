import math

num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
operator = input('Введите оператор: +, -, *, /: ')

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == "/":
        if num_2 != 0:
            print(num_1 / num_2)
        else:
            print('Ошибка: на ноль делить нельзя!!!')
    else:
        print('Вы ввели недопустимую операцию!!!')
else:
    print('Вы ввели не число, пожалуйста, введите целое число')

#################################


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

summa = num_1 + num_2 + num_3
difference = num_1 - num_2 - num_3
multiplication = num_1 * num_2 * num_3
print(summa)
print(difference)
print(multiplication)
print(num_1 - num_2 + num_3)
print(num_1 * num_2 / num_3)
print((num_1 + num_2) % num_3)

#############################


cat_a = int(input('Введите первый катет: '))
cat_b = int(input('Введите второй катет: '))

gipotenuza = math.sqrt(cat_a ** 2 + cat_b ** 2)

print(gipotenuza)

###########################

stroka = input('Введите строку: ')

kol = stroka.count(' ')
print('Количество слов: ', kol + 1)
################################

stroka = input('Введите строку: ')

a_1 = stroka[:stroka.find('h') + 1]
a_2 = stroka[stroka.find('h') + 1:stroka.rfind('h')]
a_3 = stroka[stroka.rfind('h'):]
new_stroka = a_1 + a_2.replace('h', 'H') + a_3
print(new_stroka)
################################

stroka = input('Введите строку: ')

print('Третий символ: ', stroka[2])
print('Предпоследний символ: ', stroka[-2])
print('Первые 5 символов: ', stroka[:5])
print('Все, кроме последних  двух символов: ', stroka[:-2])
print('Четные символы: ', stroka[0::2])
print('Нечетные символы: ', stroka[1::2])
print('Символы в обратном порядке: ', stroka[::-1])
print('Символы в обратном порядке через один: ', stroka[::-2])
print('Длина строки: ', len(stroka))

###################################

num = int(input('Введите  число: '))

print('Последняя цифра: ', num % 10)

################################


num = int(input('Введите трехзначное число: '))

print('Количество десятков = ', num // 10 % 10)

######################


num = int(input('Введите трехзначное число: '))

num_1 = num // 100
num_2 = num // 10 % 10
num_3 = num % 10
print('Сумма всех цифр = ', num_1 + num_2 + num_3)
