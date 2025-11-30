# AoC 2024
# Dec16
# Part 1
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
data = [l.strip() for l in open("Input/example.txt", "rt")]
#data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

the_maze = [list(line) for line in data]
print(the_maze)
for row in range(len(the_maze)):
    for col in range(len(the_maze[row])):
        if the_maze[row][col] == "S":
            start_cell = (row, col)
        if the_maze[row][col] == "E":
            end_cell = (row, col)
print(start_cell, end_cell)


def dfs(maze: list, start: tuple, end: tuple, orientation: str):
    directions = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
    cw  = ["^", ">", "v", "<", "^"]
    ccw = ["^", "<", "v", ">", "^"]
    queue = {(start, orientation): 0}
    cost = {(start, orientation): 0}

    #print(len(queue))

    while len(queue) > 0:
        this_cell = list(queue.keys())[0]
        this_cell_cost = queue.pop(this_cell)
        print("this_cell = ", this_cell, ": ", this_cell_cost)
        for direction in list(directions.keys()):
            print("direction = ", direction)
            neighbor_cell = maze[this_cell[0][0] + direction[0]][this_cell[0][1] + direction[1]]
            if neighbor_cell in [".", "E"]:
                cw_turns = abs(cw.index(directions[direction]) - cw.index(this_cell[1]))
                ccw_turns = abs(ccw.index(directions[direction]) - ccw.index(this_cell[1]))
                print("cw_turns = ", cw_turns)
                print("ccw_turns = ", ccw_turns)
                minimum_turns = min(cw_turns, ccw_turns)
                for turn in range(minimum_turns):
                    queue[(this_cell[0], directions[direction])] = 1000 + min(this_cell_cost, queue.get((this_cell[0], directions[direction]), this_cell_cost))
                    print(queue)
                
                                




dfs(the_maze, start_cell, end_cell, ">")

################
#..............#
################

solution = "Pending..."
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
