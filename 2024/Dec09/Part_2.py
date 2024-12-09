# AoC 2024
# Dec09
# Part 2

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

def swap_elements(the_list: list, idx1: int, idx2: int):
    tmp_ele = the_list[idx1]
    the_list[idx1] = the_list[idx2]
    the_list[idx2] = tmp_ele

def fs_checksum(the_list: list):
    cs = 0
    for idx in range(len(the_list)):
        if the_list[idx] >= 0:
            cs += idx * the_list[idx]
    return cs

def find_free_space(the_list: list, the_length: int, max_pos: int):
    start_pos = the_list.index(-1)
    match_pos = None
    while start_pos < max_pos and match_pos is None:
        free_length = 0
        free_pos_start = the_list.index(-1, start_pos)
        free_pos = free_pos_start
        while the_list[free_pos] == -1 and free_length < the_length:
            free_length += 1
            free_pos += 1
        if free_length >= the_length:
            match_pos = free_pos_start
        else:
            start_pos = the_list.index(-1, free_pos)

    return match_pos

def find_file_length(the_list: list, the_file_id: int):
    the_length = 0
    start_pos = the_list.index(the_file_id)
    while (start_pos + the_length) < len(the_list) and the_list[start_pos + the_length] == the_file_id:
        the_length += 1

    return the_length

file_id = 0
alternator = -1
digit_type = alternator**2
#print(digit_type)
disk_map = data[0]
block_layout = []
for ff in list(disk_map):
    for f_space in range(int(ff)):
        if digit_type == 1:
            block_layout.append(file_id)
        else:
            block_layout.append(digit_type)
        #print(ff + ': ' + str(f_space))
    if digit_type == 1:
        file_id += 1
    digit_type = digit_type * alternator

max_file_id = file_id - 1
#max_file_id = max(block_layout)
#print("max_file_id = " + str(max_file_id))

#print(block_layout)

#print(block_layout.index(-1))

#freespace = find_free_space(block_layout, 3, 32)
#print("freespace = " + str(freespace))

fid = max_file_id

#print(len(block_layout))
while fid >= 0:
    lgt = find_file_length(block_layout, fid)
    file_idx = block_layout.index(fid)
    free_idx = find_free_space(block_layout, lgt, file_idx)
    if free_idx is not None:
        for offset in range(lgt):
            swap_elements(block_layout, file_idx + offset, free_idx + offset)
    fid -= 1

#print(block_layout)

filesystem_checksum = fs_checksum(block_layout)
print("filesystem_checksum = " + str(filesystem_checksum))
