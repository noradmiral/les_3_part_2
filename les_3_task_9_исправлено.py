# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

MAX_COLUMN = 5
MAX_STR = 4
RANGE_MIN = 0
RANGE_MAX = 100

matrix = [[random.randint(RANGE_MIN, RANGE_MAX) for _ in range(MAX_COLUMN)] for _ in range(MAX_STR)]
print(*matrix, sep='\n')
print('-' * 45)

print('Минимальные по столбцам: ', end='')
#Каюсь , решение ниже помог сделать Егор , не хватило тямы самому додуматься...
max_el = RANGE_MIN - 1

for i in range(MAX_COLUMN):
    min_el = matrix[0][i]
    for i in range(MAX_STR):
        if matrix[i][i] < min_el:
            min_el = matrix[i][i]
    if max_el < min_el:
        max_el = min_el
    print(min_el, end=' ')
print()
print(f'Максимальное из минимальных: {max_el}')