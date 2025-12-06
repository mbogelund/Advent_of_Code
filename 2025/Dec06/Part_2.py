# AoC 2025
# Dec 6
# Part 2
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
#data = [l.strip() for l in open(dirname + "/Input/input.txt", "rt")]
data = [l.rstrip("\n") for l in open(dirname + "/Input/input.txt", "rt")]
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

# Convert text columns into cephalopod math numbers
def col_to_numbers(col_list: list):
    #print(col_list)
    col_width = max([len(column) for column in col_list])
    #print(col_width)
    return_list = []
    for idx in range(col_width - 1, -1, -1):
        number_text = ""
        #print(idx)
        for row in col_list:
            number_text += row[idx]
            #print(number_text)
        return_list.append(int(number_text))
        #print(return_list)
    return return_list

# Generate a list of single-row column lists from at text row
def row_to_col_lists(row: str, idx_list: list):
     return [[row[idx_list[idx_idx_list]:idx_list[idx_idx_list + 1] - 1]] for idx_idx_list in range(len(idx_list) - 1)]


# Create a list of column start indices. Add a dummy index at the end to indicate where an extra column at the end would begin
col_indices = [reg_oper.start() for reg_oper in re.finditer("\\" + "+", data[-1])] + [reg_oper.start() for reg_oper in re.finditer("\\" + "*", data[-1])]
col_indices.sort()
last_cols = [data[row][col_indices[-1]:] for row in range(len(data) - 1)]
last_col_length = max([len(col_text) for col_text in last_cols])
col_indices.append(col_indices[-1] + last_col_length + 1)

# Make a list of operators
operators = data[-1].split()

# Cenerate list with lists of text columns
row_col_list = row_to_col_lists(data[0], col_indices)
for row in data[1:len(data) - 1]:
    new_col_row = row_to_col_lists(row, col_indices)
    for col_idx in range(len(col_indices) - 1):
        row_col_list[col_idx].append(new_col_row[col_idx][0])

# Convert the list with lists of text columns to list with list of cephalopod math numbers
problem_cols = [col_to_numbers(col_list) for col_list in row_col_list]

# Calculate solutions to all cephalopod math problems
solutions = [calculate(problem_cols[iter], operators[iter]) for iter in range(len(problem_cols))]
#print(solutions)

# Sum solutions to get the overall solution
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
