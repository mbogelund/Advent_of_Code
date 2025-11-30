# AoC 2024
# Dec15
# Part 2
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

def robot_check_loc(robot_loc: tuple, move_char: str, wall_dict: dict, box_dict: dict):
    if move_char == ">":
        to_loc = (robot_loc[0], robot_loc[1] + 1)
    elif move_char == "v":
        to_loc = (robot_loc[0] + 1, robot_loc[1])
    elif move_char == "<":
        to_loc = (robot_loc[0], robot_loc[1] - 1)
    elif move_char == "^":
        to_loc = (robot_loc[0] - 1, robot_loc[1])
    
    to_loc_char = wall_dict.get(to_loc, box_dict.get(to_loc, "."))
    
    return to_loc_char, to_loc

def push_box(box_loc: tuple, move_char: str, wall_dict: dict, box_dict: dict, push_dict: dict):
    if box_dict.get(box_loc, ".") not in ["[", "]"]:
        print("Not a box at ", box_loc)
        return False
    elif box_dict.get(box_loc) == "[":
        box_char
    
    if move_char == ">":
        to_loc = (box_loc[0], box_loc[1] + 1)
    elif move_char == "v":
        to_loc = (box_loc[0] + 1, box_loc[1])
    elif move_char == "<":
        to_loc = (box_loc[0], box_loc[1] - 1)
    elif move_char == "^":
        to_loc = (box_loc[0] - 1, box_loc[1])
    
    to_loc_char = wall_dict.get(to_loc, box_dict.get(to_loc, "."))

    if move_char in ["v", "^"] and to_loc_char in ["[", "]"]:

    if to_loc_char == "#":
        return False
    elif to_loc_char == ".":
        box_dict[to_loc] = box_dict.pop(box_loc)
        return True
    elif to_loc_char == "O":
        could_push = push_box(to_loc, move_char, wall_dict, box_dict)
        if could_push:
            box_dict[to_loc] = box_dict.pop(box_loc)
        return could_push

warehouse = []
movements = []
walls = {}
wall_char = "#"
boxes = {}
box_char = "O"
box_char1 = "["
box_char2 = "]"
robot_char = "@"

at_warehouse = True
for line in data:
    if len(line) < 1:
        at_warehouse = False
    elif at_warehouse == True:
        warehouse.append(line)
    else:
        movements.append(line)

for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
        if warehouse[row][col] == wall_char:
            walls[(row, col * 2)] = wall_char
            walls[(row, col * 2 + 1)] = wall_char
        elif warehouse[row][col] == box_char:
            boxes[(row, col * 2)] = box_char1
            boxes[(row, col * 2 + 1)] = box_char2
        elif warehouse[row][col] == robot_char:
            robot_loc = (row, col * 2)


for move_line in movements:
    for move_char in move_line:
        #print(move_char)
        next_loc_char, next_loc = robot_check_loc(robot_loc, move_char, walls, boxes)
        if next_loc_char == ".":
            robot_loc = next_loc
        elif next_loc_char == "[" or next_loc_char == "]":
            pushed = push_box(next_loc, move_char, walls, boxes, {})
            if pushed:
                robot_loc = next_loc

solution = 0
for box in boxes.keys():
    solution += box[0] * 100 + box[1]

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
