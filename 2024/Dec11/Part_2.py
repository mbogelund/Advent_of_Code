# AoC 2024
# Dec11
# Part 2
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
    

def compress(stone_list: list):
    return_compressed = {}
    for stone in stone_list:
        return_compressed [stone] = return_compressed.get(stone, 0) + 1
    return return_compressed

def compressed_blink(stone_dict: dict):
    work_dict = stone_dict.copy()
    stone_dict.clear()
    for stone_eng in list(work_dict.keys()):
        tmp_stone_list = [stone_eng]
        blink(tmp_stone_list)
        for next_stone in tmp_stone_list:
            stone_dict[next_stone] = stone_dict.get(next_stone, 0) + work_dict[stone_eng]


stone_line = [int(stone_eng) for stone_eng in data[0].split(' ')]
print("Initial stone_line: ", stone_line)

iterations = 75

compressed = compress(stone_line)
for iter in range(1, iterations+1):
    compressed_blink(compressed)
    

solution = sum(compressed.values())
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
