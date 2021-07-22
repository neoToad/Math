

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def find_x_prime(x):
    with open('primes_list.txt', 'r+') as filename:
        prev_numbers = filename.read().split(',')
        new_numbers = []
        if len(prev_numbers) >= x:
            print(prev_numbers[x - 1])
        else:
            for y in range(int(prev_numbers[-1]) + 1, 1_000_000_000_000_000_000_000_000):
                if prime(y):
                    new_numbers.append(y)
                    if len(prev_numbers + new_numbers) > x + 1:
                        for item in new_numbers:
                            filename.write(',%s' % item)
                        break
            print(new_numbers[-1])


# find_x_prime(10001)