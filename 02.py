# Day 02

with open('./02.txt') as my_input:
    input_line = my_input.readline()

id_list = [tuple(map(int, ids.split('-'))) for ids in input_line.split(',')]

invalid_ids = []
all_invalid_ids = []
for first_id, last_id in id_list:
    for id_num in range(first_id, last_id + 1):
        id_num = str(id_num)
        id_len = len(id_num)
        if not id_len % 2:
            if id_num[:id_len//2] == id_num[id_len//2:]:
                invalid_ids.append(id_num)
        pattern = ''
        for digit in id_num[:id_len//2]:
            pattern += digit
            if pattern*(id_len//len(pattern)) == id_num:
                all_invalid_ids.append(id_num)
                break

# Part 1

print(sum(map(int, invalid_ids)))

# Part 2


print(sum(map(int, all_invalid_ids)))
