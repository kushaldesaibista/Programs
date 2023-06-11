

n = int(input("Enter a natural number"))


def square_sum(n):
    return 0 if (n==0) else n**2 + square_sum(n-1)


print(square_sum(n))