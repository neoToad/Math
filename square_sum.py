
class Difference:
    def __init__(self, number):
        self.number = number

    def find_difference(self):
        """Find the difference"""
        self.squares = self.sum_of_squared()
        self.squares_added = self.add_numbers(self.squares)
        self.number_added = self.add_numbers(range(self.number + 1))
        self.naturals_squared = self.squared(self.number_added)
        self.difference = self.dif_nat_from_sqr(self.naturals_squared, self.squares_added)
        self.print_message()

    def print_message(self):
        """Print message to the user"""
        print(f"The squares of 1 to {self.number} added is {self.squares_added}\n"
              f"The numbers of 1 to {self.number} added is {self.number_added}\n"
              f"{self.number_added} squared is {self.naturals_squared}\n"
              f"The difference between {self.naturals_squared} and {self.squares_added}"
              f" is {self.difference}.")


    def sum_of_squared(self):
        return [x ** 2 for x in range(1, self.number + 1)]

    def add_numbers(self, sum_of_list):
        sum = 0
        for num in sum_of_list:
            sum += num
        return sum

    def squared(self, num):
        return num ** 2

    def dif_nat_from_sqr(self, nat, sqr):
        return nat - sqr

ten = Difference(int(input("Enter a number:")))
ten.find_difference()