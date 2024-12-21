# AoC 2024
# Dec17
# Part 1
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

register = {}
for line in data:
    if len(line) > 0:
        if line[:8] == "Register":
            print(line)
            register[line.split(":")[0].split()[1]] = int(line.split(":")[1])
        elif line[:7] == "Program":
            program = [int(instr) for instr in line.split(":")[1].split(",")]

print(register)
print(program)

def computer(reg: dict, pgm: list):
    work_reg = reg.copy()
    instr_ptr = 0
    combo_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg["A"], 5: reg["B"], 6: reg["C"], 7: None}
    output = []
    while instr_ptr < len(pgm):
        #print(instr_ptr)
        instr = pgm[instr_ptr]
        instr_ptr_incr = 2
        oper = pgm[instr_ptr + 1]

        #print("Instruction: ", instr, ". Operand: ", oper)
        if   instr == 0: # adv
            work_reg["A"] = work_reg["A"] >> combo_map[oper]
            #print("Register A should be: ",work_reg["A"] // (2**combo_map[oper]), ". It is: ", work_reg["A"])
        elif instr == 1: # bxl
            #print("Register B binary: ",bin(work_reg["B"]))
            work_reg["B"] = work_reg["B"] ^ oper
            #print("oper binary: ", bin(oper), ". Register B binary: ",bin(work_reg["B"]))
        elif instr == 2: # bst
            work_reg["B"] = combo_map[oper] & 0b111
            #print("Register B should be: ",work_reg["B"] % 8, ". It is: ", work_reg["B"])
        elif instr == 3: # jnz
            if bool(work_reg["A"]):
                instr_ptr = oper
                instr_ptr_incr = 0
                #print("instr_ptr: ", instr_ptr, ". oper: ", oper, ". instr_ptr_incr: ", instr_ptr_incr)
            else:
                #print("Doing nothing...")
                pass
        elif instr == 4: # bxc
            #print("Register B binary: ", bin(work_reg["B"]), ". Register C binary: ",bin(work_reg["C"]))
            work_reg["B"] = work_reg["B"] ^ work_reg["C"]
            #print("Register B binary: ", bin(work_reg["B"]))
        elif instr == 5: # out
            #print(oper, combo_map[oper], combo_map[oper] & 0b111)
            output.append(combo_map[oper] & 0b111)
            #print("Appended ", combo_map[oper] % 8, ". Output is now: ", output)
        elif instr == 6: # bdv
            work_reg["B"] = work_reg["A"] >> combo_map[oper]
            #print("Register B should be: ",work_reg["A"] // (2**combo_map[oper]), ". It is: ", work_reg["B"])
        elif instr == 7: # cdv
            work_reg["C"] = work_reg["A"] >> combo_map[oper]
            #print("Register C should be: ",work_reg["A"] // (2**combo_map[oper]), ". It is: ", work_reg["C"])

        if bool(instr_ptr_incr):
            combo_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: work_reg["A"], 5: work_reg["B"], 6: work_reg["C"], 7: None}
        #print("work_reg = ", work_reg)
        instr_ptr += instr_ptr_incr
    return output


result = computer(register, program)

#print(result)

solution = ','.join([str(num) for num in result])

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
