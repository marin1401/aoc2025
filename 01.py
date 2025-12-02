# Day 01

import math

with open('./01.txt') as my_input:
    input_lines = my_input.readlines()

def multiples_of_100_in_range(a, b):
    return math.floor(max(a, b)/100) - math.ceil(min(a, b)/100) + 1

instructions = [(line[0], int(line[1:])) for line in input_lines]

number = 50
zero_position_counter = 0
zero_pass_counter = 0
for rotation, distance in instructions:
    previous_number = number
    if rotation == 'L':
        number -= distance
    elif rotation == 'R':
        number += distance
    if not number % 100:
        zero_position_counter += 1
    zero_pass_counter += multiples_of_100_in_range(previous_number, number)

#Part 1

print(zero_position_counter)

# Part 2


print(zero_pass_counter - zero_position_counter)
