while True:
    file_name = input('Название файла: ')

    sym = file_name.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')'))
    extension = file_name.endswith('.txt') or file_name.endswith('.docx')

    if sym:
        print('\nОшибка: название начинается на один из специальных символов.')
    elif not extension:
        print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('\nФайл назван верно.')
        break