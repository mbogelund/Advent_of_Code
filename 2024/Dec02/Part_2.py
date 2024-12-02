# AoC 2024
# Dec02
# Part 2

import re

# Import today's data
#data = [l.strip().split() for l in open("Input/example.txt", "rt")]
data = [l.strip().split() for l in open("Input/input.txt", "rt")]
#print(data)

def is_it_safe(strline):
    #print('strline: ')
    #print(strline)
    line = [int(element) for element in strline]
    monotone = (line == sorted(line)) or (line == sorted(line)[::-1])
    maxdif = max([abs(int(line[idx]) - int(line[idx + 1])) for idx in range(len(line) - 1)])
    mindif = min([abs(int(line[idx]) - int(line[idx + 1])) for idx in range(len(line) - 1)])
    safe = int(monotone == True) * int(maxdif <= 3) * int(mindif >= 1)
    return safe

safe = 0
for reportline in data:
    safe_report = is_it_safe(reportline)
    if safe_report < 1:
        #print(reportline)
        safe_report = max([is_it_safe(reportline[:idx] + reportline[idx+1:]) for idx in range(len(reportline))])
        #print(safe_report)
        

    safe += safe_report

print()
print("Safe: " + str(safe))
