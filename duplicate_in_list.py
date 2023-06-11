# duplicate from a list count


list_1 = [1, 2, 3, 4, 5, 2, 2, 1, 5, 7, 6]
unique = []
printing_list = []
no_duplicate_list = []

# for i in list_1:
#     if i not in unique:
#         unique.append(i)
#         print("uniq")
#         print(unique)
#     elif i not in printing_list:
#         printing_list.append(i)
#         print("printing")
#         print(printing_list)

for i in list_1:
    if i not in unique:
        unique.append(i)
    elif i not in printing_list:
        printing_list.append(i)

for i in unique:
    if i not in printing_list:
        no_duplicate_list.append(i)

print(unique)
print(no_duplicate_list)
print(printing_list)
