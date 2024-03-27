def tuple_name(name_temp):
    return tuple(name_temp.split())


def search_contact(surname):
    for i in dict_contact:
        if i[1] == surname:
            print(i[0], i[1], dict_contact[i])


dict_contact = {}

while True:
    print('Введите номер действия:\n'
          '\t1. Добавить контакт\n' 
          '\t2. Найти человека '
    )
    enter_user = int(input())
    if enter_user == 1:
        enter_name = input('Введите имя и фамилию нового контакта (через пробел): ').title()
        
        if tuple_name(enter_name) in dict_contact:
            print('Такой человек уже есть в контактах.')
        else:
            enter_phone = int(input('Введите номер телефона: '))
            dict_contact[tuple_name(enter_name)] = enter_phone

    elif enter_user == 2:
        enter_surname = input('Введите фамилию для поиска: ').title()
        search_contact(enter_surname)

    print(f'Текущий словарь контактов: {dict_contact}')
