
n = int(input("Enter a natural number"))


def cube_sum(n):
    return 0 if (n == 0) else n ** 3 + cube_sum(n - 1)


print(cube_sum(n))
