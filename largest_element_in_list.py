list1 = [1, 2, 2, 34, 5, 7]
largest = list1[0]
for i in range(0, len(list1) - 1):
    largest = list1[i] if list1[i] > largest else largest

print("List sum = ", largest)
