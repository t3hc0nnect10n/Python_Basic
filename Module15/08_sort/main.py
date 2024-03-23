original_list = []
for i in range(1, 5 + 1):
    original_list.append(int(input(f'Введите {i} число: ')))
print(f'Изначальный список: {original_list}')

for num in range(len(original_list) - 1):
        for i in range(len(original_list) - 1 - num):
            if original_list[i] > original_list[i + 1]:
                original_list[i], original_list[i + 1] = original_list[i + 1], original_list[i]
print(f'Отсортированный список: {original_list}')