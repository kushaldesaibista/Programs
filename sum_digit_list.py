# duplicate from a list count


list_1 = [11, 23, 32, 41, 51, 21, 22, 11, 56, 79, 96]
list2 = []


def add_digits(number, l):
    return 0 if (l < 10) else (number % 10) + add_digits(int(number / 10), l / 10)


for i in range(0, len(list_1)):
    list2.append(add_digits(list_1[i], 10 ** len(str(list_1[i]))))

print(list2)