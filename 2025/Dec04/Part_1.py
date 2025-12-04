# AoC 2025
# Dec 4
# Part 1
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

def roll_count(row_text: str, idx: int):
    roll_count = 0
    row_text_length = len(row_text)
    if idx >= 0 and idx <= row_text_length - 1:
        if row_text[idx] == "@":
            roll_count += 1
        if idx > 0:
            if row_text[idx - 1] == "@":
                roll_count += 1
        if idx < row_text_length - 1:
            if row_text[idx + 1] == "@":
                roll_count += 1
    return roll_count

rows = len(data)

movable_rolls = 0

for row_idx in range(rows):
    row = data[row_idx]
    if row_idx == 0:
        row_above = ""
    else:
        row_above = data[row_idx - 1]
    if row_idx >= rows - 1:
        row_below = ""
    else:
        row_below = data[row_idx + 1]
    
    for col_idx in range(len(row)):
        if row[col_idx] == "@":
            neighbor_rolls = roll_count(row_above, col_idx) + (roll_count(row, col_idx) - 1) + roll_count(row_below, col_idx)
            if neighbor_rolls < 4:
                movable_rolls += 1


solution = movable_rolls # Assign value of solution

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
