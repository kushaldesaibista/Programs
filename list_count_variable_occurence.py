list_a = [1, 2, 2, 2, 4, 2, 1, 9, 'a', 'b', 'a']

check = input("enter a character/value to be counted:")
check = check if check.isalpha() else int(check)
count = 0


for i in list_a:
    print(i, check, count)
    if i == check:
        count = count + 1

print(count)
