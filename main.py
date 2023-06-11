#Break list into chunks of n size


list_size = int(input("Enter list size:"))

list_value = []
for i in range(list_size):
    list_value.append(int(input(f"enter list value {i +1}:")))

block_size = int(input("divide list into:"))
count = 0
new_list = []
for i in range(0, list_size -1, block_size):
    temp_list = []
    for j in range(i, i + block_size):
        temp_list.append(list_value[j])
    new_list.append(temp_list)

print(new_list)
# new_list[i][j] = list_value[j]