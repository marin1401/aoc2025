# Day 08

import math

with open('./08.txt') as my_input:
    input_lines = my_input.readlines()

def get_3d_distance(box_1, box_2):
    return sum((box_1[i] - box_2[i])**2 for i in range(3))

boxes = [tuple(map(int, line.split(','))) for line in input_lines]

distances = []
for i, box_1 in enumerate(boxes[:-1]):
    for box_2 in boxes[i+1:]:
        distances.append((get_3d_distance(box_1, box_2), box_1, box_2))

circuits = []
for pair, (distance, box_1, box_2) in enumerate(sorted(distances), start=1):
    match = []
    for i, circuit in enumerate(circuits):
        if box_1 in circuit or box_2 in circuit:
            match.append(i)
    if not match:
        circuits.append({box_1, box_2})
    elif len(match) == 1:
        circuits[match[0]].add(box_1)
        circuits[match[0]].add(box_2)
    else:
        circuit = set.union(*(circuits[i] for i in match), {box_1, box_2})
        circuits = [circ for i, circ in enumerate(circuits) if i not in match]
        circuits.append(circuit)
    if pair == 1000:
        circuits_sizes = sorted((len(circ) for circ in circuits), reverse=True)
    if len(circuits[0]) == len(boxes):
        x_coords = (box_1[0], box_2[0])
        break

# Part 1

print(math.prod(circuits_sizes[:3]))

# Part 2

print(math.prod(x_coords))
