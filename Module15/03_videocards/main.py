videocard_list = []
count_videocard = int(input('Количество видеокарт: '))
for i in range(1, count_videocard + 1):
    videocard_num = int(input(f'{i} Видеокарта: '))
    videocard_list.append(videocard_num)
print(f'Старый список видеокарт: {videocard_list}')

videocard_list_new= [i for i in videocard_list if i < max(videocard_list)]
print(f'Новый список видеокарт: {videocard_list_new}')

