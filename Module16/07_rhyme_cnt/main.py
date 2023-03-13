human = int(input('Количество человек: '))
out = int(input('Какое число в считалке? '))

print(f'Значит, выбывает каждый {out}-й человек.')

human_list = list(range(1, human + 1))
count = 0

for _ in range(human - 1):
    print(f'\nТекущий круг людей: {human_list}')

    start_count = count % len(human_list)
    count = (start_count + out - 1) % len(human_list)

    print(f'Начало счёта с номера {human_list[start_count]}')
    print(f'Выбывает человек под номером {human_list[count]}')

    human_list.remove(human_list[count])

print(f'\nОстался человек под номером {human_list[0]}')