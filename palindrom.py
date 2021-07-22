def is_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


def find_largest_palindrome():
    largest_palindrome = ''
    for x in range(900, 1000):
        for y in range(900, 1000):
            num = x * y
            if is_palindrome(str(num)):
                largest_palindrome = num

    print(largest_palindrome)

find_largest_palindrome()
print(is_palindrome(str(909)))