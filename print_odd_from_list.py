list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]


def odd(list_odd):
    temp = []
    for i in list_odd:
        if i % 2 != 0:
            temp.append(i)
    return temp


print(odd(list_of_numbers))
