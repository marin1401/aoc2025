# Day 11

with open('./11.txt') as my_input:
    input_lines = my_input.readlines()

def count_all_paths(device):
    if device == 'out':
        return 1
    return sum(count_all_paths(next_device) for next_device in devices[device])

def count_paths(start, end, memo):
    if start == end:
        return 1
    if start in memo:
        return memo[start]
    total = 0
    for device in devices.get(start, []):
        total += count_paths(device, end, memo)
    memo[start] = total
    return total

devices = {line.split(': ')[0]: line.split()[1:] for line in input_lines}

# Part 1

print(count_all_paths('you'))

# Part 2

segments = (('svr', 'fft'), ('fft', 'dac'), ('dac', 'out'))
paths_with_fft_and_dac = 1
for start, end in segments:
    paths_with_fft_and_dac *= count_paths(start, end, {})

print(paths_with_fft_and_dac)