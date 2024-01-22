def summ(name_i, pizza_i, amount_i):
    name_i[pizza_i] = name_i.setdefault(pizza_i, 0) + int(amount_i)
    return name_i


num_order = int(input('Введите количество заказов: '))
order = {}
for num in range(1, num_order + 1):
    name, pizza, amount = input(f'{num} заказ: ').rsplit(maxsplit=3)
    order[name] = summ(order.get(name, {}), pizza, amount)

for name in sorted(order):
    print(f'{name}:')
    for pizza, amount in sorted(order.get(name).items()):
        print(f'\t\t{pizza}: {amount}')
    print()