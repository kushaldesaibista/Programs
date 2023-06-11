# interchange list elemebt
list = ['a', 'b', 'c']


def interchange(list, element1pos, element2pos):
    list[element1pos - 1], list[element2pos - 1] = list[element2pos - 1], list[element1pos - 1]
    return list


print(interchange(list, 1, 2))
