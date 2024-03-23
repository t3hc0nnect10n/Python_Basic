container_list = []
count_num = int(input('Количество контейнеров: '))
for i in range(1, count_num +1):
    mass = int(input('Введите вес контейнера: '))
    if mass <= 200:
        container_list.append(mass)

index = 0
user_enter = int(input('Введите вес нового контейнера: '))
while index < len(container_list) and container_list[index] >= user_enter:
    index += 1
print(f'Номер, который получит новый контейнер: {index + 1}')