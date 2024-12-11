# AoC 2024
# Dec11
# Part 1
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

stonemap = {0: [1]}
print(stonemap)
occurrences = {0: 0}

def map_stone(stone_engraving: int):
    return_stones = stonemap.get(stone_engraving, None)
    new_count = occurrences.get(stone_engraving, 0) + 1
    occurrences[stone_engraving] = new_count
    if return_stones is None:
        if len(str(stone_engraving))%2 == 0:
            #print(str(stone_engraving))
            return_stones = [int(str(stone_engraving)[:len(str(stone_engraving))//2]), int(str(stone_engraving)[len(str(stone_engraving))//2:])]
            #print(return_stones)
        if return_stones is None:
            return_stones = [stone_engraving * 2024]
        stonemap[stone_engraving] = return_stones

    return return_stones

def blink(stone_list: list):
    work_list = stone_list.copy()
    stone_list.clear()
    while len(work_list) > 0:
        stone_list.extend(map_stone(work_list.pop(0)))
    

stone_line = [int(stone_eng) for stone_eng in data[0].split(' ')]
#print("Initial stone_line: ", stone_line)
iterations = 25

for iter in range(1, iterations+1):
    blink(stone_line)
    #print(iter, ": ", stone_line)

#print(stonemap)

solution = len(stone_line)
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
