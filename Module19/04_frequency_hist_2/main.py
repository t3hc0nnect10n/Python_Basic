string = input('Введите текст: ')

hist = {sym: string.count(sym) for sym in string}

print('\nОригинальный словарь частот:')
for key in sorted(hist.keys()):
    print(key, ':', hist[key])

# invert_hist = {val: [i_key for i_key in hist.keys() if hist[i_key] == val] for val in set(hist.values())}

print('\nИнвертированный словарь частот:')
invert_hist = {}
for key in hist.keys():
    val = hist[key]
    if val not in invert_hist:
        invert_hist[val] = []
    invert_hist[val].append(key)

for key in sorted(invert_hist.keys()):
    print(key, ':', invert_hist[key])