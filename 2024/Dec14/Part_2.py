# AoC 2024
# Dec14
# Part 2
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

def print_robots(robot_dict: dict, width, height):
    heres_a_robot = list(robot_dict.values())
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in heres_a_robot:
                line += "R"
            else:
                line += "."
        print(line)
                

robots = {}
robot_id = 0
for line in data:
    pos_str = line.split()[0].split("=")[1]
    vel_str = line.split()[1].split("=")[1]
    robots[robot_id] = (int(pos_str.split(",")[0]), int(pos_str.split(",")[1]), int(vel_str.split(",")[0]), int(vel_str.split(",")[1]),)
    robot_id += 1

print(robots)

robots_new = {}
seconds_start = 1
seconds = 0 # Put in the max seconds you want to eyeball
seconds_step = 1
#width = 11
width = 101
#height = 7
height = 103

for second in range(seconds_start, seconds, seconds_step):
    for robot_id in list(robots.keys()):
        if second == seconds_start:
            factor = seconds_start
        else:
            factor = seconds_step
        new_x = (robots[robot_id][0] + factor * robots[robot_id][2]) % width
        new_y = (robots[robot_id][1] + factor * robots[robot_id][3]) % height
        robots_new[robot_id] = (new_x, new_y)
        robots[robot_id] = (new_x, new_y, robots[robot_id][2], robots[robot_id][3])
    
    print_robots((robots_new), width, height)
    print("Seconds: ", second)
    input("Any key to continue...")
    print()
    print()
    print("#####################################################################")
    print()
    print()
    
    #print(robots_new)
    
# In the robot images, the robots are organized in a long stretch at A seconds, and then every 101 (width) seconds after that, ie.
# A, 101 + A, 2 * 101 + A, etc.
# Also, they are lumped together at B seconds, and then every 103 (height) seeconds after that ie.
# B, 103 + B, 2 * 103 + B, etc
# Idea: Maybe the easter egg appears when "lumpy" meets "stretch", ie. when x * 101 + A = y * 103 + B, x and y being integers.
#
# x = (y * 103 + B - A) / 101

A = 0 # Put in the value you found
B = 0 # Put in the value you found
for y in range(1, 200):
    x = (y * height + B - A) / width
    if x == int(x):
        print("x = ", x, ", y = ", y)
        print(x * width + A)
        print(y * height + B)
        break

for robot_id in list(robots.keys()):
    second = y * height + B
    new_x = (robots[robot_id][0] + second * robots[robot_id][2]) % width
    new_y = (robots[robot_id][1] + second * robots[robot_id][3]) % height
    robots_new[robot_id] = (new_x, new_y)
    robots[robot_id] = (new_x, new_y, robots[robot_id][2], robots[robot_id][3])
    
print_robots((robots_new), width, height)


#print_robots((robots_new), width, height)

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
