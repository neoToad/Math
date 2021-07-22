import itertools
import math


def add_divisors(n, divisor_list):
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):
            # If divisors are equal, print only one
            if (n / i == i):
                divisor_list.append(i),
            else:
                # Otherwise print both
                divisor_list.append(int(n / i))
                divisor_list.append(i)
        i = i + 1


def find_t_number():
    divisors = []
    tried_nums = []

    tri_num = 0
        # Find tri-numbers
    for i in itertools.count(start=1):
        tri_num += i
        # print(i)

        if tri_num not in tried_nums:
            # get divisors of tri numbers
            add_divisors(tri_num, divisors)
            print(f'iteration: {i}, tri-number: {tri_num}, number of divisors: {len(divisors)}')

        tried_nums.append(tri_num)
            # print(len(divisors))
        if len(divisors) > 500:
            print(tried_nums[-1])
            break
        divisors = []
find_t_number()
