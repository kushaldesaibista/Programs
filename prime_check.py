#prime

prime_check = int(input("enter a number"))
flag_prime = False
for i in range(2, int(prime_check/2)):
    if prime_check % i == 0:
        flag_prime = True
        break

if flag_prime:
    print("prime")
else:
    print("not prime")
