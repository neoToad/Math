from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)



# def div_1_to_10(n):
#     found = False
#     tried = 1
#     count = 0
#     while not found:
#         for x in range(1, n + 1):
#             if tried % x == 0:
#                 count += 1
#                 if count >= n:
#                     print(tried)
#                     found = True
#
#             else:
#                 tried += 1
#                 count = 0
#                 break

# div_1_to_10(5)
print(reduce(lcm, range(1, 21)))