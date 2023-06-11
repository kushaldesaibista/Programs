list_positive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 56, 7, 9, 65, 45, 66, 12, 34]

start = 10
end = 100


def even_range(start, end):
    temp = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            temp.append(i)
    return temp


print(even_range(4, 10))


def even_in_list_range(start, end, list_positive):
    temp = []
    for i in list_positive:
        if start < i < end:
            if i % 2 == 0:
                temp.append(i)

    return temp


print(even_in_list_range(start, end, list_positive))
