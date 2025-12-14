# Day 09

with open('./09.txt') as my_input:
    input_lines = my_input.readlines()

def get_area(x_1, y_1, x_2, y_2):
    return (abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1)

def border_crossed(x_min, x_max, y_min, y_max):
    for (x_1, y_1), (x_2, y_2) in zip(tiles, tiles[1:] + [tiles[0]]):
        x_check = max(x_1, x_2) > x_min and min(x_1, x_2) < x_max
        y_check = max(y_1, y_2) > y_min and min(y_1, y_2) < y_max
        if x_check and y_check:
            return True
    return False

tiles = [tuple(map(int, line.split(','))) for line in input_lines]

areas = set()
areas_in_bounds = set()
for i, (x_1, y_1) in enumerate(tiles[:-1]):
    for x_2, y_2 in tiles[i+1:]:
        areas.add(get_area(x_1, y_1, x_2, y_2))
        if not border_crossed(*sorted((x_1, x_2)), *sorted((y_1, y_2))):
            areas_in_bounds.add(get_area(x_1, y_1, x_2, y_2))

# Part 1

print(max(areas))

# Part 2

print(max(areas_in_bounds))