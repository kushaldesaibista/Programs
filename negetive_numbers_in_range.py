# negative numbers in range

start = int(input("Start value:"))
end = int(input("End value:"))


def negative_numbers_in(start, end):
    return_list = []
    if start < end:
        for i in range(start, end):
            if i < 0:
                return_list.append(i)
    return return_list


print(negative_numbers_in(start, end + 1))
