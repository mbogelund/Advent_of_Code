# AoC 2024
# Dec03
# Part 2

import re

# Import today's data
#data = [l.strip() for l in open("Input/example2.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

enabled = True
data2 =[]
for strline in data:
    workline = strline
    while len(workline) > 0:
        if enabled:
            line_split = re.split(r"don\'t\(\)", workline, 1)
            data2.append(line_split[0])
        if not enabled:
            line_split = re.split(r"do\(\)", workline, 1)

        if len(line_split) > 1:
            workline = line_split[1]
            enabled = not enabled
        else:
            workline = ''
        
        #print(line_split)

print(data2)


sum_of_products = 0
for strline in data2:
    occurrences = re.findall(r"mul\(\d+,\d+\)", strline)
    #print(occurrences)
    for mul in occurrences:
        #print(mul)
        num1 = int(re.split(',', re.split(r"\(", mul)[1])[0])
        #print(num1)
        num2 = int(re.split(',', re.split(r"\(", mul)[1])[1].replace(')', ''))
        #print(num2)
        sum_of_products += num1 * num2
print("Sum of products: " + str(sum_of_products))
