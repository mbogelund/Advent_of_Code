# AoC 2025
# Dec 1
# Part 2
import datetime
import re
import os

start_time = datetime.datetime.now()

# Import today's data
basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
print(dirname)
print(basename)
#data = [l.strip() for l in open(dirname + "/Input/example.txt", "rt")]
data = [l.strip() for l in open(dirname + "/Input/input.txt", "rt")]
print(data)
print("----------------")

def rot_to_int(rot: str):
    sign = 0
    if rot[0] == "L":
        sign = -1
    if rot[0]  == "R":
        sign = 1
    return sign * int(rot[1:])

def zero_pass(pos: int, prev_pos: int):
    abs_diff = abs(pos - prev_pos)

    # If difference is a multiple of 100, it's the difference divided by 100
    if abs_diff % 100 == 0:
        return abs_diff // 100

    
    # Create downshifts - think of them as the lower bound of an interval between 2 neighboring whole hundreds 
    pos_downshift = pos // 100 * 100
    prev_pos_downshift = prev_pos // 100 * 100

    # If difference is under 100, it's either 0 or 1
    if abs_diff < 100:
        if pos_downshift != prev_pos_downshift and prev_pos % 100 != 0 or pos % 100 == 0:
            return 1
        return 0
    
    # If difference is over 100, it's the difference divided by 100, unless it's a left turn
    #  and we either come to or from a position that is a whole hundred
    if abs_diff > 100:
        adjust = 0
        if prev_pos > pos and prev_pos % 100 == 0:
            adjust = -1
        if prev_pos > pos and pos % 100 == 0:
            adjust = 1
        return abs(pos_downshift - prev_pos_downshift) // 100 + adjust

prev_position = 50
position = prev_position
zero_count = 0
for rotation in data:
    position += rot_to_int(rotation)
    #print(prev_position, position)
    zp = zero_pass(position, prev_position)
    zero_count += zp
    #print(rotation, zero_count)
    prev_position = position



solution = zero_count # Assign value of solution

################
#..............#
################

#solution = "Pending..."
print("#--------------------#")
print("Solution: ", solution)
print("#--------------------#")
print()

# Timer
print("############# TIMER ##############")
end_time = datetime.datetime.now()
print("Start time: ", start_time)
print("End time: ", end_time)
print("Time used: ", end_time-start_time)
