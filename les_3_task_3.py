# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Если таких элементов несколько, то меняем любой максимальный на любой минимальный:


import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив:', array, sep='\n')

num_min = array[0]
min_index = 0
num_max = array[0]
max_index = 0

for i, item in enumerate(array):
    if item < num_min:
        num_min = item
        min_index = i
    elif item > num_max:
        num_max = item
        max_index = i

print(f'Меняем число {num_max} с индексом {max_index} местами с числом {num_min} с индексом {min_index}.\n')

array[max_index], array[min_index] = array[min_index], array[max_index]
print('Новый массив:', array, sep='\n')


# Вариант 2
# import random
#
# r = [random.randint(0, 99) for _ in range(10)]
# print(f'Массив до изменения: {r}')
#
# max = r[0]
# min = r[0]
#
# for i in r:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# min_index = r.index(min)
# max_index = r.index(max)
# r[min_index], r[max_index] = r[max_index], r[min_index]
# print(f'Массив осле изменения элементов {min_index} и {max_index}: {r}')