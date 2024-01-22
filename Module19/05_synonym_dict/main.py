num = int(input('Введите количество пар слов: '))

dict_synonyms = {}
for i in range(1, num + 1):
    few_words = input(f'{i} пара: ').title().split(' - ')
    dict_synonyms[few_words[0]] = few_words[1]

print(dict_synonyms)

while True:
    word = input('Введите слово: ').title()

    if word in dict_synonyms.keys():
        result = dict_synonyms.get(word)
        print('Синоним: ', result)
        break
    elif word in dict_synonyms.values():
        result = list(dict_synonyms.keys())[list(dict_synonyms.values()).index(word)]
        print('Синоним: ', result)
        break
    else:
        print('Такого слова в словаре нет.')