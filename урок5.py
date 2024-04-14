# import math
#
# x = 0
# for n in range(0, 8):
#     x = (-1) ** n * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
#     print(math.sin(x))

# for n in range(0, 1000):
#     (-1) ** n * ((x ** 2 * n) / math.factorial(2 * n))
#     print(math.cos(x))


"""2 задача"""

# N = int(input('Сколько денег надо накопить Маше на новый телефон? '))
# k = int(input('Сколько денег Маша может накопить каждый день? '))
# cash = 0
# days = 0
#
# while cash < N:
#
#     days += 1
#     if days % 7 != 0:
#         cash += k
#         print('Маша уже накопила', cash, 'рублей')
#         print('Осталось накопить', N - cash, 'рублей')
#
# print('Маша накопила', cash, 'рублей', 'за', days, 'дней')


"""3 задача"""

# num_list = []
#
#
# while len(num_list) != 15:
#     if len(num_list) > 1:
#         num_list.append(num_list[-1] + num_list[-2])
#     else:
#         num_list.append(1)
# print(num_list)


"""4 задача"""

# num_list = [2, 7, 13, 345, 23, 0, -5, -1224, 45345, -43443, 346, 3, 5, -67]
#
# sum_kol = 0
# min_elem = 0
# max_elem = 0
#
# for i in num_list:
#     if min_elem > i:
#         min_elem = i
#     if max_elem < i:
#         max_elem = i
# for i in num_list:
#     sum_kol += i
# print('Минимальный элемент в списке = ', min_elem)
# print('Максимальный элемент в списке = ', max_elem)
# print('Сумма элементов в списке = ', sum_kol)


"""5 задача"""

'''Дан список чисел. Реализовать программу, которая проверит, все
ли числа в списке уникальны (встречаются только один раз).
Программа должна вывести результат проверки, и, если не все
элементы уникальны, вывести дублирующиеся элементы и
количество их повторений в списке'''

# num_list = [1, 1, 2, 2, 3, 3, 4, 5, 5]
# new_list = []
# counter = 0
# for i in range(len(num_list)):
#     for j in range(i + 1, len(num_list)):
#         if num_list[i] == num_list[j]:
#             counter += 1
#             new_list.append(num_list[i])
# print('количество повторений в списке = ', counter)
# print(new_list)
#


"""6 задача"""

# num_list = [1, 4, 7, 10, 13, 18, 24, 56]
#
# elem = int(input('Введите элемент: '))
#
# index_elem = 0
# high_elem = len(num_list) - 1
# mid_elem = len(num_list) // 2
#
# while num_list[mid_elem] != elem and index_elem <= high_elem:
#     if elem > num_list[mid_elem]:
#         index_elem = mid_elem + 1
#     else:
#         high_elem = mid_elem - 1
#     mid_elem = (index_elem + high_elem) // 2
# if index_elem > high_elem:
#     print('Нет элементов')
# else:
#     print(mid_elem)

"""7 задача"""

num_list = [5, 6, 7, 1, 2, 3, 4]
new_list = num_list[::]
num_list.sort()
elem = int(input('Введите элемент: '))

index_elem = 0
high_elem = len(num_list) - 1
mid_elem = len(num_list) // 2

while num_list[mid_elem] != elem and index_elem <= high_elem:
    if elem > num_list[mid_elem]:
        index_elem = mid_elem + 1
    else:
        high_elem = mid_elem - 1
    mid_elem = (index_elem + high_elem) // 2
if index_elem > high_elem:
    print('Нет элементов')
else:
    print(num_list[mid_elem])
x = num_list[mid_elem]
print(new_list)
print(new_list.index(x))
