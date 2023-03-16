def get_index(symbol, step_right, alphabet_list):
    index = alphabet_list.index(symbol)

    if index + step_right > len(alphabet_list) - 1:
        index = index + step_right - len(alphabet_list)
    else:
        index += step_right
    return index


text = input('Введите сообщение: ').lower()
step = int(input('Введите сдвиг: '))

alphabet = [chr(i) for i in range(ord('а'), ord('а') + 32)]
encrypted_text = ''

for sym in text:
    if sym in alphabet:
        encrypted_text += alphabet[get_index(sym, step, alphabet)]
    else:
        encrypted_text += sym

print(encrypted_text)