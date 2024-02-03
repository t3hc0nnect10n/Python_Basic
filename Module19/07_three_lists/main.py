array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1.')

array_4 = [i for i in array_1 if i in array_2 and i in array_3]
print('Решение без множеств: ', end='')
print(*array_4, sep=', ')

set_array_4 = set(array_1).intersection(array_2, array_3)
print('Решение с множествами: ', end='')
print(*set_array_4, sep=', ')

print('\nЗадача 2')
array_4 = [i for i in array_1 if i not in array_2 and i not in array_3]
print('Решение без множеств: ', end='')
print(*array_4, sep=', ')

set_array_4 = set(array_1) - set(array_2).union(array_3)
print('Решение с множествами: ', end='')
print(*set_array_4, sep=', ')