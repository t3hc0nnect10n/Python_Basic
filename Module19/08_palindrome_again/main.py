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
    return True

    new_pali = ''
    if middle:
        new_pali = middle * counts[middle]
    for letter in counts:
        if letter != middle:
            new_pali = letter * int(counts[letter] / 2) + new_pali + letter * int(counts[letter] / 2)
    return new_pali


word = input('Введите строку: ')
if palindrome(word):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')