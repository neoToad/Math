def open_content(x):
    with open(x) as f:
        c_list = [x for x in f.read()]
        c_list = list(filter(('\n').__ne__, c_list))
        return [int(x) for x in c_list]


class FindAdjProduct:
    def __init__(self, content):
        self.highest_adj = []
        self.highest_value = 0
        self.content = open_content(content)
        self.content_product = self.content[:]
        self.num_adjacent = 0

    def find_highest_product(self, num_adjacent):
        # find product of adjacent numbers
        self.num_adjacent = num_adjacent
        while True:
            self.find_product_of_arr()
            if len(self.content_product) < num_adjacent:
                print(self.highest_value)
                print(self.highest_adj)
                return False

    def find_product_of_arr(self):
        self.count = 0
        self.value = 1
        self.adj_nums = []
        for x in self.content_product:
            self.value *= x
            self.count += 1
            self.adj_nums.append(x)
            self.reset_arr()

    def reset_arr(self):
        if self.count >= self.num_adjacent:
            if self.value > self.highest_value:
                self.highest_adj = self.adj_nums[:]
                self.highest_value = self.value
            self.count = 0
            self.value = 1
            self.adj_nums.clear()
            self.content_product.pop(0)


highest_adj = FindAdjProduct('content.txt')
highest_adj.find_highest_product(13)

