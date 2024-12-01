# AoC 2024
# Dec01
# Part 2

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
#print(data)

left_list = list()
right_list = list()

for line in data:
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

#print(left_list)
#print(right_list)

left_list.sort()
right_list.sort()

#print(left_list)
#print(right_list)

similarity_score = 0
for idx in range(len(left_list)):
    similarity_score += left_list[idx] * right_list.count(left_list[idx])

print("Solution: " + str(similarity_score))
