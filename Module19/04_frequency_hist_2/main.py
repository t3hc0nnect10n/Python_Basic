string = input('Введите текст: ')

hist = {sym: string.count(sym) for sym in string}

print('\nОригинальный словарь частот:')
for key in sorted(hist.keys()):
    print(key, ':', hist[key])

invert_hist = {val: [i_key for i_key in hist.keys() if hist[i_key] == val] for val in set(hist.values())}

print('\nИнвертированный словарь частот:')
for invert_key in invert_hist:
    print(f'{invert_key} : {invert_hist[invert_key]}')