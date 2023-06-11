import math as m


# fibonacci series


def fib(f0, f1, n, k, rangefib):
    l1 = []
    for i in range(0, rangefib + 1):
        l1.append(f0)
        f0, f1 = f1, f0 + f1

    return l1


print(fib(0, 1, 4, 12,100))


def isPerfectSquare(check):
    return int(m.sqrt(check)) * int(m.sqrt(check)) == check


def search_fin(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


print(search_fin(4))
