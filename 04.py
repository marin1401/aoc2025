# Day 04

with open('./04.txt') as my_input:
    grid = my_input.read().splitlines()

def count_neighbouring_rolls(current_y, current_x, current_rolls):
    counter = -1
    for y in range(-1,2):
        for x in range(-1,2):
            if (current_y + y, current_x + x) in current_rolls:
                counter += 1
    return counter

def get_next_rolls(current_rolls, next_rolls):
    for y, x in rolls:
        if count_neighbouring_rolls(y, x, rolls) > 3:
            next_rolls.add((y, x))
    return next_rolls

rolls = set()
for y, row in enumerate(grid):
    for x, column in enumerate(row):
        if grid[y][x] == '@':
            rolls.add((y, x))
rolls_number = len(rolls)

# Part 1

print(rolls_number - len(get_next_rolls(rolls, set())))

# Part 2

while True:
    next_rolls = get_next_rolls(rolls, set())
    if len(rolls) == len(next_rolls):
        print(rolls_number - len(rolls))
        break

    rolls = {roll for roll in next_rolls}
