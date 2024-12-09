# AoC 2024
# Dec09
# Part 1

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

#print(block_layout)

#print(block_layout.index(-1))

blockpos = -1
#print(len(block_layout))


while len(block_layout) + blockpos > block_layout.index(-1):
    #print(blockpos)
    swap_elements(block_layout, blockpos, block_layout.index(-1))
    blockpos -= 1

#print(block_layout)

filesystem_checksum = fs_checksum(block_layout)
print("filesystem_checksum = " + str(filesystem_checksum))
