# AoC 2025
# Dec 1
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

def rot_to_int(rot: str):
    sign = 0
    if rot[0] == "L":
        sign = -1
    if rot[0]  == "R":
        sign = 1
    return sign * int(rot[1:])


position = 50
zero_count = 0
for rotation in data:
    position += rot_to_int(rotation)
    if position % 100 == 0:
        zero_count += 1

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
