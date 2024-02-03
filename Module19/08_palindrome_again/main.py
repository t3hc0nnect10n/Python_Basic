from collections import defaultdict


def palindrome(our_string):
    our_string = our_string.lower()
    counts = defaultdict(int)
    for letter in our_string:
        if 97 <= ord(letter) <= 122:
            counts[letter] += 1

    middle = ''
    for letter in counts:
        if middle and counts[letter] % 2 == 1:
            return False
        elif counts[letter] % 2 == 1:
            middle = letter

    new_palindrom = ''
    if middle:
        new_palindrom = middle * counts[middle]
    for letter in counts:
        if letter != middle:
            new_palindrom = letter * int(counts[letter] / 2) + new_palindrom + letter * int(counts[letter] / 2)

    return True, print(f'Палиндром: {new_palindrom}')



word = input('Введите строку: ')
if palindrome(word):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')