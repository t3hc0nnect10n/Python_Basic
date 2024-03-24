students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)


def infoInterestsSurname(students_data):
    interests_list = []
    surname_string = ''
    for i in students_data:
        i_interests = students_data[i]['interests']
        interests_list.extend(i_interests)
        i_surname = students[i]['surname']
        surname_string += i_surname
    interests_set = set(interests_list)

    return interests_set, len(surname_string)


interests, surname_len = infoInterestsSurname(students)
id_age = [(id, students.get(id, {}).get('age', {})) for id in students]

print(f'\nСписок пар "ID студента — возраст": {id_age}\n'
      f'Полный список интересов всех студентов: {interests}\n'
      f'Общая длина всех фамилий студентов: {surname_len}'
)