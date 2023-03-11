first_class = []
second_class = []
new_class = []

for i in range(160, 178, 2):
    first_class.append(i)
print(f'Первый класс: {first_class}')

for i in range(162, 183, 3):
    second_class.append(i)
print(f'Второй класс: {second_class}')

new_class.extend(sorted(first_class + second_class))
print(f'Отсортированный список учеников: {new_class}')

