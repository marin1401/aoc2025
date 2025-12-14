# Day 12

with open('./12.txt') as my_input:
    input_lines = my_input.read().splitlines()

lines = [line for line in input_lines if 'x' in line]
regions = [tuple(map(int, line.split(':')[0].split('x'))) for line in lines]
quantities = [sum(map(int, line.split()[1:])) for line in lines]

print(sum(a*b >= quantity*9 for (a, b), quantity in zip(regions, quantities)))