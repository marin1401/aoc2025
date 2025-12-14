# Day 10

import numpy as np
from itertools import combinations
from scipy.optimize import milp, LinearConstraint

with open('./10.txt') as my_input:
    input_lines = my_input.readlines()

def min_light_press(lights_goal, buttons):
    for press in range(1, len(buttons) + 1):
        for combination in combinations(buttons, press):
            lights = [0] * len(lights_goal)
            for button in combination:
                for position in button:
                    lights[position] ^= 1
            if lights == lights_goal:
                return press

def min_jolt_press(joltages_goal, buttons):
    joltages_goal = np.asarray(joltages_goal, dtype=int)
    m = len(joltages_goal)
    n = len(buttons)
    A = np.zeros((m, n), dtype=int)
    for j, button in enumerate(buttons):
        for i in button:
            A[i, j] = 1
    c = np.ones(n, dtype=int)
    lb = np.zeros(n, dtype=int)
    ub = np.zeros(n, dtype=int)
    for i in range(n):
        mask = A[:, i].astype(bool)
        ub[i] = joltages_goal[mask].min()
    cons = LinearConstraint(A, joltages_goal, joltages_goal)
    intg = np.ones(n, dtype=bool)
    res = milp(c=c, bounds=(lb, ub), constraints=cons, integrality=intg)
    return int(res.fun)

min_light_presses = []
min_jolt_presses = []
for line in input_lines:
    lights, *buttons, joltages = line.split()
    lights = [light == '#' for light in lights[1:-1]]
    buttons = [tuple(map(int, button[1:-1].split(','))) for button in buttons]
    joltages = tuple(map(int, joltages[1:-1].split(',')))
    min_light_presses.append(min_light_press(lights, buttons))
    min_jolt_presses.append(min_jolt_press(joltages, buttons))

# Part 1

print(sum(min_light_presses))

# Part 2

print(sum(min_jolt_presses))