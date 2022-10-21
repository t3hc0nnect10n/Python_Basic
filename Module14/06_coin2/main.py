def scan(x, y, r):
    return (x * x + y * y) ** 0.5 < r


print('Введите координаты монетки:')
point_x = float(input('X: '))
point_y = float(input('Y: '))
radius = int(input('Введите радиус: '))

if scan(point_x, point_y, radius):
    print('Монетка где-то рядом.')
else:
    print('Монетки в области нет.')
