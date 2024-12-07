# AoC 2024
# Dec07
# Part 1

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

results_tree = {}

# Recursive function to read/calculate an expression from a list of integers and operators
def calculate(cal_list: list):
    if len(cal_list) == 1:
        return int(cal_list[0])
    if results_tree.get(''.join(cal_list), None) == None:
        if cal_list[-2] == '+':
            results_tree[''.join(cal_list)] = calculate(cal_list[:-2]) + int(cal_list[-1])
        elif cal_list[-2] == '*':
            results_tree[''.join(cal_list)] = calculate(cal_list[:-2]) * int(cal_list[-1])
    return results_tree.get(''.join(cal_list), None)

#test_list = ['7', '+', '19', '*', '3']
#x = calculate(test_list)
#print('x=' + str(x))
#print(results_tree)

# Function that traverses all the possible permutations of expressions from a list of integers, and looks for the target result
def find_result(cal_val_list: list, result: int):
    operators = {48: 43, 49: 42}
    permutations = [list((bin(perm_num)[2:].zfill(len(cal_val_list) - 1)).translate(operators)) for perm_num in range(2**(len(cal_val_list) - 1))]
    #print(permutations)
    
    found = False
    
    for permutation in permutations:
        expr_list = []
        for idx in range(len(cal_val_list) - 1):
            expr_list.append(cal_val_list[idx])
            expr_list.append(permutation[idx])
        expr_list.append(cal_val_list[-1])
        #print(expr_list)
        expr_result = calculate(expr_list)
        #print('expr_result=' + str(expr_result))
        if result == expr_result:
            found = True
            #print("Found result!")
            break
    return found

#test_list2 = ['7', '19', '3']
#found_it = find_result(test_list2, 79)
#print(found_it)


total_calibration_result = 0

for strline in data:
    test_value = int(strline.split(':')[0])
    #print(test_value)
    cal_values = strline.split(':')[1].split()
    #print(cal_values)
    if find_result(cal_values, test_value):
        total_calibration_result += test_value

print("Total calibration result: " + str(total_calibration_result))
    

