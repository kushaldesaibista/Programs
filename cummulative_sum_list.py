# duplicate from a list count


list_1 = [1, 2, 3, 4, 5, 2, 2, 1, 5, 7, 6]
sum = []
for i in range(0, len(list_1)):
    if i == 0:
        sum.append(list_1[i])
    else:
        sum.append(list_1[i] + sum[i - 1])

print(sum)



