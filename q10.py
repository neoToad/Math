from number_of_primes import prime

sum_of_primes = 0
highest_prime = 2_000_000


def sundaram3(max_n):
    """ Use Sieve of Sundaram to return list of prime numbers quickly"""

    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))


list_of_primes = sundaram3(8011010) # Save as list

# check for last number in list as sometimes odd numbers that are not prime
# make it into the list
if not prime(list_of_primes[-1]):
    list_of_primes.pop(-1)

print(sum(list_of_primes))