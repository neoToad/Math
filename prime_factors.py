import math
prime_factors = []


def find_prime_factors(x):
    while x % 2 == 0:
        prime_factors.append(2)
        x = x / 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        # while i divides x , append i and divide x
        while x % i == 0:
            prime_factors.append(i)
            x = x / i
            # Condition if n is a prime
        # number greater than 2
    if x > 2:
        prime_factors.append(x)
    return prime_factors


print(find_prime_factors(60085147))