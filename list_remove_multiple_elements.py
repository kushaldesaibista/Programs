# remove multiple elements from list
original_list = [-2, -5, -3, -1, 3, 6, 12, -1]

print("original list:", original_list)

elements_to_be_removed = int(input("Enter the number of elements to be removed:"))
removing_elements = []
for i in range(0, elements_to_be_removed):
    temp = int(input("enter element"))
    for j in range(0, len(original_list)):
        if temp in original_list:
            original_list.remove(temp)

print(removing_elements)

print("list after removing element", original_list)
