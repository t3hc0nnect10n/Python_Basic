def functionZip(string_i, numbers_i):
    return ((string_i[i], numbers_i[i]) for i in range(min(len(string_i), len(numbers_i))))


string = 'abcd'
numbers = (10, 20, 30, 40)
without_functionZip = ((string[i], numbers[i]) for i in range(min(len(string), len(numbers))))

print(f'Строка: {string}\n'
      f'Кортеж чисел: {numbers}\n\n'
      f'Результат:\n'
      f'{functionZip(string, numbers)}\n'
      f'{without_functionZip}'
)
result_tuple = [print((i, x)) for i, x in zip(string, numbers)]
