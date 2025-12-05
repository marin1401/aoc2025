# Day 05

with open('./05.txt') as my_input:
    input_string = my_input.read()

def join_ranges(first_id_check, last_id_check, id_range):
    for first_id, second_id in id_range:
        if first_id < first_id_check <= second_id:
            return (first_id, max(second_id, last_id_check))
        elif first_id <= last_id_check < second_id:
            return (min(first_id, first_id_check), second_id)
    return False

fresh_ids, available_ids = input_string.split("\n\n")

fresh_ids = {tuple(map(int, ids.split("-"))) for ids in fresh_ids.splitlines()}

# Part 1

fresh_available_ids = set()
for available_id in map(int, available_ids.splitlines()):
    for first_id, last_id in fresh_ids:
        if first_id <= available_id <= last_id:
            fresh_available_ids.add(available_id)

print(len(fresh_available_ids))

# Part 2

while True:
    for first_id, last_id in list(fresh_ids):
        if (new_range := join_ranges(first_id, last_id, fresh_ids)):
            fresh_ids.remove((first_id, last_id))
            fresh_ids.add(new_range)
            break
    else:
        break

counter = 0
for first_id, last_id in fresh_ids:
    counter += last_id - first_id + 1

print(counter)