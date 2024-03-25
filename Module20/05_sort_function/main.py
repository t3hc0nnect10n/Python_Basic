tpl = (6, 3, -1, 8, 4, 10, -5)


def tpl_sort(temp):

    for i_num in temp:
        if not isinstance(i_num, int):
            return temp
            break
    else:
        list_isinstance_int = tuple(sorted(list(num for num in temp)))

        return list_isinstance_int


print(tpl_sort(tpl))
