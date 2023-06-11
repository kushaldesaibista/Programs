
list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]

def even(list_even):
    temp = []
    for i in list_even:
        if i % 2 == 0:
            temp.append(i)
    return temp


print(even(list_of_numbers))
