list1 = [11, -21, 0, 45, 66, -93]


# negative values only without zero

def negative_numbers(list1):
    list2 = []
    for i in list1:
        if i < 0:
            list2.append(i)

    return list2


print(negative_numbers(list1))
