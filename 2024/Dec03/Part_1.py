# AoC 2024
# Dec03
# Part 1

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

sum_of_products = 0
for strline in data:
    occurrences = re.findall(r"mul\(\d+,\d+\)", strline)
    print(occurrences)
    for mul in occurrences:
        print(mul)
        num1 = int(re.split(',', re.split(r"\(", mul)[1])[0])
        print(num1)
        num2 = int(re.split(',', re.split(r"\(", mul)[1])[1].replace(')', ''))
        print(num2)
        sum_of_products += num1 * num2
print("Sum of products: " + str(sum_of_products))
