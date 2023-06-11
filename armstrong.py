"""armstrong"""

number = 153
l = 10 ** len(str(number))


def armstrong(number, l):
    return 0 if (l < 10) else (number % 10) ** 3 + armstrong(int(number / 10), l / 10)


if (armstrong(number, l) == number):
    print("armstrong:{0}".format(number))
