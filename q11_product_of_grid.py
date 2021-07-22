grid = []

with open("grid.txt", "r") as f:
    for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        grid.append(line_list)


# for x in grid:
#     print(x)

def grid_pos(x, y):
    try:
        return grid[x][y]
    except IndexError:
        print(str(x) + ' ' + str(y) + " coordinates has an error")

def multiply_list(int_list):
    product = 1
    for num in int_list:
        product *= num
    return product


class HighestGridProduct:
    def __init__(self, grid):
        self.grid = grid
        self.highest_product = 0

        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if rows - row > 3:
                    self.find_product_down(row, column)
                if columns - column > 3:
                    self.find_product_across(row, column)
                if rows - row > 3 and columns - column > 3:
                    self.find_product_diagonal_right(row, column)
                if rows - row > 3 and column - 4 > 0:
                    self.find_product_diagonal_left(row, column)

        print(self.highest_product)

    def find_product_down(self, x, y):
        multiply = []
        while 4 > len(multiply):
            multiply.append(int(grid_pos(x, y)))
            x += 1
        current_product = multiply_list(multiply)
        self.check_highest_product(current_product)
        print(f"product of {multiply} is {current_product}")

    def find_product_across(self, x, y):
        multiply = []
        while 4 > len(multiply):
            multiply.append(int(grid_pos(x, y)))
            y += 1
        current_product = multiply_list(multiply)
        self.check_highest_product(current_product)

    def find_product_diagonal_right(self, x, y):
        multiply = []
        while 4 > len(multiply):
            multiply.append(int(grid_pos(x, y)))
            x += 1
            y += 1

    def find_product_diagonal_left(self, x, y):
        multiply = []
        while 4 > len(multiply):
            multiply.append(int(grid_pos(x, y)))
            x += 1
            y -= 1


        current_product = multiply_list(multiply)

        self.check_highest_product(current_product)

    def check_highest_product(self, current_product):
        if current_product > self.highest_product:
            self.highest_product = current_product

highest_product = HighestGridProduct(grid)
