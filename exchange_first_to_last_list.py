# interchange list elemebt
l1 = ['a', 'b', 'c']


def interchange(l1):
    l1[0], l1[-1] = l1[-1], l1[0]
    return l1


print(interchange(l1))
