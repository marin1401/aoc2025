# Day 07

with open('./07.txt') as my_input:
    manifold = my_input.read().splitlines()

splitters = set()
beam = set()
qbeam = {}
for y, row in enumerate(manifold):
    for x, column in enumerate(row):
        if manifold[y][x] == "^":
            splitters.add((y, x))
        elif manifold[y][x] == "S":
            beam_start = (y+1, x)
            beam.add(beam_start)
            qbeam[beam_start] = 1

# Part 1

counter = 0
for y, row in enumerate(manifold):
    for x, column in enumerate(row):
        if (y, x) in beam:
            if (y+1, x) in splitters:
                beam.add((y+1, x-1))
                beam.add((y+1, x+1))
                counter += 1
            elif y < len(manifold)-1:
                beam.add((y+1, x))

print(counter)

# Part 2

for y, row in enumerate(manifold):
    for x, column in enumerate(row):
        if (y, x) in qbeam.keys():
            if (y+1, x) in splitters:
                qbeam[(y+1, x-1)] = qbeam.get((y+1, x-1), 0) + qbeam[(y, x)]
                qbeam[(y+1, x+1)] = qbeam.get((y+1, x+1), 0) + qbeam[(y, x)]
            elif (y+1, x) in qbeam.keys():
                qbeam[(y+1, x)] += qbeam[(y, x)]
            else:
                qbeam[(y+1, x)] = qbeam[(y, x)]

print(sum(v for k, v in qbeam.items() if k[0] == len(manifold)-1))