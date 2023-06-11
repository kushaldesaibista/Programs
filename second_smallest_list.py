list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]


def findSecondSmallest(lst):
    firstSmallest = lst[0] if lst[0] < lst[1] else lst[1]
    secondSmallest = lst[0] if lst[0] > lst[1] else lst[1]
    for i in range(2, len(lst)):
        if lst[i] < firstSmallest:
            secondSmallest = firstSmallest
            firstSmallest = lst[i]
        elif lst[i] < secondSmallest and firstSmallest < lst[i]:
            secondSmallest = lst[i]
    return secondSmallest


print(findSecondSmallest(list_of_numbers))

# Output:
1