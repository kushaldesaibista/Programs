list1 = [1,2,2,34,5,7]
smallest = list1[0]
for i in range(0, len(list1)-1):
    smallest = list1[i] if list1[i] < smallest else smallest

print("List sum = ", smallest)