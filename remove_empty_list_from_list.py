

test_list = [5, 6, [], 3, [], [], 9]


print("The original list is : " + str(test_list))


reverse_list = [element for element in test_list if element != []]

print(reverse_list)