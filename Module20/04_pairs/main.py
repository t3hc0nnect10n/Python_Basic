number_list = [i for i in range(0, 10)]
new_number_list = list(zip(number_list[::2], number_list[1::2]))
print(f'Оригинальный список: {number_list}\n'
      f'Новый список: {new_number_list}')
