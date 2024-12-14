# AoC 2024
# Dec05
# Part 1

import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

orderings = [tuple(page_order.split('|')) for page_order in [order for order in data if '|' in order]]
print(orderings)

print_pages = [pages for pages in data if ',' in pages]
#print(print_pages)

right_order = []
reverse_order = []

solution = 0
for print_job in print_pages:
    correct_order = True
    pages = print_job.split(',')
    #print("pages = ", pages)
    reverse_order.clear()
    for page1_idx in range(len(pages) - 1):
        for page2_idx in range(page1_idx + 1, len(pages)):
            if (pages[page2_idx], pages[page1_idx]) in orderings:
                #print("Ordering violated! " + pages[page2_idx] + "," + pages[page1_idx])
                correct_order = False
            reverse_order.append((pages[page2_idx], pages[page1_idx]))
    #print(correct_order)
    if correct_order:
        solution += int(pages[len(pages) // 2])
    #print("reverse_order = ", reverse_order)


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
