# AoC 2024
# Dec13
# Part 1
import datetime
import re

from sympy import symbols, Eq, solve

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

x, y = symbols('x y')
eq_parms =[]
machine_imported = False
solution = 0
for row_num in range(len(data)):
    if len(data[row_num]) < 1:
        machine_imported = False
        eq_parms.clear()
        #print("next_machine")
    if len(data[row_num]) > 0:
        #print(data[row_num])
        line = data[row_num]
        tmp_str = line[:6]
        if tmp_str == "Button":
            button = line.split()[1][0]
            eq_parms.append(int(line.split()[2].split('+')[1].split(',')[0]))
            eq_parms.append(int(line.split()[3].split('+')[1].split(',')[0]))
            #print(button)
            #print(eq_parms[-2])
            #print(eq_parms[-1])
        if tmp_str == "Prize:":
            eq_parms.append(int(line.split()[1].split('=')[1].split(',')[0]) + 10000000000000)
            eq_parms.append(int(line.split()[2].split('=')[1].split(',')[0]) + 10000000000000)
            machine_imported = True
            #print("Prize")
            #print(eq_parms[-2])
            #print(eq_parms[-1])
    if machine_imported == True:
        #print("eq_parms = ", eq_parms)
        eq1 = Eq(eq_parms[0] * x + eq_parms[2] * y, eq_parms[4])
        eq2 = Eq(eq_parms[1] * x + eq_parms[3] * y, eq_parms[5])
        eq_solution = solve((eq1, eq2), (x, y))
        #print("eq_solution = ", eq_solution)
        
        #print(eq_solution[x] == int(eq_solution[x]))
        #print(eq_solution[y] == int(eq_solution[y]))
        if eq_solution[x] == int(eq_solution[x]) and eq_solution[y] == int(eq_solution[y]):
            solution += int(eq_solution[x]) * 3 + int(eq_solution[y]) * 1
        
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
