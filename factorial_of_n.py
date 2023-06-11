n = int(input("Enter a positive integer for factorial: "))


def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)


print("factorial of !{0} is {1}".format(n, factorial(n)))
