number_1 = 10
number_2 = 20

max = lambda number_1, number_2: number_1 if number_1 > number_2 else number_2

print("Maximum of {0} and {1} is {2}" .format(number_1, number_2, max(number_1, number_2)))
