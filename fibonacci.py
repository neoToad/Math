

def fibonacci_sequence(max_number):
    fibonacci_sequence = [1, 2]
    x = 1
    y = 2
    sum = x + y
    while sum < max_number:
        x = y
        y = sum
        fibonacci_sequence.append(sum)
        sum += x
    return fibonacci_sequence

def sum_of_evens(to_check):
    sum = 0
    for x in to_check:
        if x % 2 == 0:
            sum += x
    print(sum)
    
four_mil = fibonacci_sequence(4_000_000)

sum_of_evens(four_mil)