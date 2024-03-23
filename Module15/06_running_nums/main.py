list_1 = [1, 2, 3, 4, 5]
list_temp = []
step = int(input('Сдвиг: '))
while step <= len(list_1):
    i = list_1[-step:] + list_1[:-step]
    list_temp.append(i)
    step += 1

print(f'Изначальный список: {list_1}')
print(f'Сдвинутый список: {list_temp[0]}')
