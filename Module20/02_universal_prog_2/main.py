import math
string = 'О Дивный Новый мир!'
list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Алгоритм O(n)
def isNumber_On(temp):


    def isPrime_On(n):
        if n > 1:
            for i in range(2, (n // 2) + 1):
                if (n % i) == 0:
                    return False
            else:
                return True


    list_prime = [i[1] for i in enumerate(temp) if isPrime_On(i[0])]
    return list_prime


# Алгоритм O(sqrt(n))
def isNumber_O_sqrt_n(temp):


    def isPrime_O_sqrt_n(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


    list_prime = [i[1] for i in enumerate(temp) if isPrime_O_sqrt_n(i[0])]
    return list_prime


print(f'Варинат O(n)\n'
      f'Ответ в консоли: {isNumber_On(list_number)}\n'
      f'Ответ в консоли: {isNumber_On(string)}\n\n'
      f'Варинат O(sqrt(n))\n'
      f'Ответ в консоли: {isNumber_O_sqrt_n(list_number)}\n'
      f'Ответ в консоли: {isNumber_O_sqrt_n(string)}'
)