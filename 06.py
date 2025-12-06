# Day 06

import math

with open('./06.txt') as my_input:
    input_lines = my_input.readlines()

def get_total(numbers, operator):
    if operator == '+':
        total = sum(numbers)
    elif operator == '*':
        total = math.prod(numbers)
    return total

# Part 1

all_numbers = [tuple(map(int, line.split())) for line in input_lines[:-1]]
operators = input_lines[-1].split()

grand_total = 0
for i, operator in enumerate(operators):
    numbers = (numbers[i] for numbers in all_numbers)
    grand_total += get_total(numbers, operator)

print(grand_total)

# Part 2

operators_line = input_lines[-1]
current_operator = ''
numbers = []
grand_total = 0
for i, character in enumerate(operators_line):
    current_operator = character if character != ' ' else current_operator
    col_nums = [nums[i] for nums in input_lines[:-1] if nums[i] != ' ']
    if col_nums:
        numbers.append(int(''.join(col_nums)))
    if not col_nums or i+1 == len(operators_line):
        grand_total += get_total(numbers, current_operator)
        numbers = []

print(grand_total)