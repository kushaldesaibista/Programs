
print("Enter two numbers")
a = float(input("Enter no.1"))
b = float(input("Enter no.2"))


def add(a, b):
    v = a+ b
    return v


print("sum of {0} and {1} is {2}".format(a, b, add(a, b)))
