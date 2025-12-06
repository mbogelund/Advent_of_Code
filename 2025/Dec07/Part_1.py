# AoC 2025
# Dec 6
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
data = [l.strip() for l in open(dirname + "/Input/example.txt", "rt")]
#data = [l.rstrip("\n") for l in open(dirname + "/Input/example.txt", "rt")]
#data = [l.rstrip("\n") for l in open(dirname + "/Input/input.txt", "rt")]
#data = [l.strip() for l in open(dirname + "/Input/input.txt", "rt")]
print(data)
print("----------------")


solution = None # Assign value of solution

################
#..............#
################

solution = "Pending..."
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
