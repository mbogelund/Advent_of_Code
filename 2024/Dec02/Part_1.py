# AoC 2024
# Dec02
# Part 1

import re

# Import today's data
#data = [l.strip().split() for l in open("Input/example.txt", "rt")]
data = [l.strip().split() for l in open("Input/input.txt", "rt")]
#print(data)

safe = 0
for strline in data:
    line = [int(element) for element in strline]
    #print(line)
    monotone = (line == sorted(line)) or (line == sorted(line)[::-1])
    #print(sorted(line))
    #print(monotone)
    maxdif = max([abs(int(line[idx]) - int(line[idx + 1])) for idx in range(len(line) - 1)])
    #print(maxdif)
    mindif = min([abs(int(line[idx]) - int(line[idx + 1])) for idx in range(len(line) - 1)])
    #print(mindif)
    safe += int(monotone == True) * int(maxdif <= 3) * int(mindif >= 1)
    #print(safe)

print()
print("Safe: " + str(safe))
