# Day 03

with open('./03.txt') as my_input:
    banks = my_input.read().splitlines()

# Part 1

joltages = []
for bank in banks:
    first_battery, second_battery = 0, 0
    for battery, next_battery in zip(bank, bank[1:]):
        battery, next_battery = map(int, (battery, next_battery))
        if battery > first_battery:
            first_battery = battery
            second_battery = next_battery
        elif next_battery > second_battery:
            second_battery = next_battery
    joltages.append(str(first_battery) + str(second_battery))

print(sum(map(int, joltages)))

# Part 2

joltages = []
for bank in banks:
    batteries = []
    primary_position = 0
    while len(batteries) < 12:
        bank_range = bank[primary_position:len(bank)+len(batteries)-11]
        for secondary_position, battery in enumerate(bank_range):
            if battery == max(bank_range):
                batteries.append(battery)
                primary_position += secondary_position + 1
                break
    joltages.append("".join(batteries))

print(sum(map(int, joltages)))