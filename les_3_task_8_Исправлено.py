# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
# элементов строк. Программа должна вычислять сумму введенных элементов
# каждой строки и записывать в последнюю ячейку строки. В конце следует
# вывести полученную матрицу.


MAX_COLUMN = 4
MAX_STR = 5

result_list = []
sum_el = 0
for d in range(MAX_STR):
    result_list.append([])
    for i in range(MAX_COLUMN - 1):
        el = int(input(f'Введите {i + 1} элемент {d + 1} строки: '))
        result_list[d].append(el)
        sum_el += el
    result_list[d].append(sum_el)
    sum_el = 0

print('Итоговая матрица 5х4')
for el in result_list:
    for i in el:
        print(f'{i:>5}', end='')
    print()
#Второй вариант , точнее первый но показалось что не правильно решил,хотя он тоже рабочий )
# matrix = []
#
# for i in range(5):
#     matrix.append([])
#     sum_= 0
#     for n in range(3):
#         user_number = int(input(f'Введите элемент {i+1} и {n+1} столбца: '))
#         sum_ += user_number
#         matrix[i].append(user_number)
#
#     matrix[i].append(sum_)
#
# for a in matrix:
#     print(('{:>3d}' * 4).format(*a))
#Переделал , в первый раз не правильное расположение матрици было, поменял пару циферок и вроде по заданию все ))