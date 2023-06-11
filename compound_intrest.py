def calc_simple_intrest(principal, time, rate, n):
    R = rate / 100
    amount = principal * (1 + R / n) ** (time * n)
    print(amount)


calc_simple_intrest(1000, 12, 0.1, 1)
