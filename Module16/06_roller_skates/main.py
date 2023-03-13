skates_list = []
human_list = []
count = 0

skates = int(input('Количество коньков: '))
for i in range(skates):
    size_skate = int(input(f'Размер пары {i + 1}: '))
    skates_list.append(size_skate)

human = int(input('Количество людей: '))
for num_hum in range(human):
    size_man = int(input(f'Размер ноги человека {num_hum + 1}: '))
    human_list.append(size_man)

for num_skate in human_list:
    if num_skate in skates_list:
        skates_list.remove(num_skate)
        count += 1

print(f'Наибольшее количество людей, которые могут взять ролики: {count}')