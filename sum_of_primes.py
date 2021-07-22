

class Answer:
    def __init__(self, highest_number):
        self.value = 0
        self.highest_number = highest_number

    def check_start(self):
        if self.highest_number > 100_000:
            self.value = 454396537
            start = 100_000
            self.find_sum_of_primes(start)

    def find_sum_of_primes(self, start):

        for x in range(start, self.highest_number):
            if self.prime(x):
                self.value += x
                print(self.value)
        print(self.value)

    def prime(self, num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    def check_if_multiple(self, number, number2):
        total = 0
        for x in range(self.highest_number):
            if x % number == 0 or x % number2 == 0:
                    total += x
                    print(x)
        print(total)


question_01 = Answer(1000)

question_01.check_if_multiple(3, 5)