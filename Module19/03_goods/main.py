goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key in goods.keys():
    sum_price = 0
    sum_count = 0

    for i_value in range(len(store[goods[key]])):
        sum_price += store[goods[key]][i_value]['quantity'] * store[goods[key]][i_value]['price']
        sum_count += store[goods[key]][i_value]['quantity']

    print(f'{key} - {sum_count} шт, стоимость {sum_price} руб')
