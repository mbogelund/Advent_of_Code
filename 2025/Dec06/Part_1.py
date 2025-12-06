# AoC 2025
# Dec 6
# Part 1
import datetime
import re
import os
import math

start_time = datetime.datetime.now()

# Import today's data
basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
print(dirname)
print(basename)
#data = [l.strip() for l in open(dirname + "/Input/example.txt", "rt")]
#data = [l.rstrip("\n") for l in open(dirname + "/Input/example.txt", "rt")]
data = [l.strip() for l in open(dirname + "/Input/input.txt", "rt")]
#data = [l.rstrip("\n") for l in open(dirname + "/Input/input.txt", "rt")]
print(data)
print("----------------")

# Calculate product or sum of each sublist's elements, based on corresponding operator in operators list
def calculate(num_list: list, oper: str):
    if oper != '+' and oper != '*':
        print("ERROR!")
    if oper == '+':
        return sum(num_list)
    if oper == '*':
        return math.prod(num_list)

# Make list of operators
operators = data[-1].split()
print(operators)

#problem_column = [data[row][0][idx_idx_next]]

# Make list of list with numbers for each problem
problems = [[int(num) for num in [row.split()[idx] for row in data[:len(data) - 1]]] for idx in range(len(operators))]
print(problems)
# Calculate solutions
solutions = [calculate(problems[iter], operators[iter]) for iter in range(len(problems))]
print(solutions)

# Calculate overall solution
solution = sum(solutions) # Assign value of solution

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
