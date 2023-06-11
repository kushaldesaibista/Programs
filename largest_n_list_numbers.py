import heapq as hq

list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]


def nLargest(largest_list, cycle):
    n_largest = []

    for j in range(cycle):
        temp = 0
        for i in range(0, len(largest_list)):
            if temp < largest_list[i]:
                temp = largest_list[i]
        n_largest.append(temp)
        largest_list.remove(temp)

    return n_largest


print(nLargest(list_of_numbers, 3))


#  Output:
# def nLargest(list_n, largest):
#     list_n.sort()
#     print(list_n[-largest:])
#
#
# def nLargest(list_n, largest):
#     print(hq.nlargest(largest, list_n))
