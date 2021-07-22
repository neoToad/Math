large_num_sum = []

with open("large_sum.txt", "r") as f:
    for line in f:
        stripped_line = line.strip()
        large_num_sum.append(int(stripped_line))


print(str(sum(large_num_sum))[:10])