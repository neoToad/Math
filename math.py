# def check_if_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             return True
#
#
# def find_factors(num):
#     factors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     return factors
#
#
# def find_prime_factors(factors_list):
#     prime_factors = []
#     for factor in factors_list:
#         if check_if_prime(factor):
#             prime_factors.append(factor)
#     return prime_factors
#
#
# def find_prime_numbers(number):
#     prime_numbers = []
#     # Find prime numbers
#     for num in range(number + 1):
#         if check_if_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers
#
# factors = find_factors(6008514)
# print(factors)

import math


def maxPrimeFactor(n):
   # number must be even

   while n % 2 == 0:
      max_Prime = 2
      n /= 1
   # number must be odd

   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
         max_Prime = i
         n = n / i
   # prime number greator than two

   if n > 2:
      max_Prime = n
   return int(max_Prime)

# Driver code to test above function

n = 1445
print(maxPrimeFactor(n))