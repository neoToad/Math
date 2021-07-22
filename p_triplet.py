

def squared(x):
    return x ** 2

def check_if_ptrip(a, b, c):
    if squared(a) + squared(b) == squared(c):
        print("Correct")
        print(a, b, c)
        return True


def add_three_factors():
    for x in range(500):
        for y in range(501):
            for z in range(1001):
                check_if_ordered(x, y, z)


def check_if_ordered(x, y, z):
    if x < y < z:
        if x + y + z == 1000:
            if check_if_ptrip(x, y, z):
                print(f"{x} < {y} < {z}\n"
                      f"{x} + {y} + {z} == 1000")

                
# add_three_factors()

print(200 * 375 * 425)