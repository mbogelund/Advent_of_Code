# AoC 2024
# Dec14
# Part 1
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

robots = {}
robot_id = 0
for line in data:
    pos_str = line.split()[0].split("=")[1]
    vel_str = line.split()[1].split("=")[1]
    robots[robot_id] = (int(pos_str.split(",")[0]), int(pos_str.split(",")[1]), int(vel_str.split(",")[0]), int(vel_str.split(",")[1]),)
    robot_id += 1

#print(robots)

robots_new = {}
seconds = 100
#width = 11
width = 101
#height = 7
height = 103
for robot_id in list(robots.keys()):
    new_x = (robots[robot_id][0] + seconds * robots[robot_id][2]) % width
    new_y = (robots[robot_id][1] + seconds * robots[robot_id][3]) % height

    robots_new[robot_id] = (new_x, new_y)

#print(robots_new)

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot_id in list(robots_new.keys()):
    if robots_new[robot_id][0] < width // 2 and robots_new[robot_id][1] < height // 2:
        q1 += 1
    if robots_new[robot_id][0] > width // 2 and robots_new[robot_id][1] < height // 2:
        q2 += 1
    if robots_new[robot_id][0] < width // 2 and robots_new[robot_id][1] > height // 2:
        q3 += 1
    if robots_new[robot_id][0] > width // 2 and robots_new[robot_id][1] > height // 2:
        q4 += 1

#print("q1 = ", q1)
#print("q2 = ", q2)
#print("q3 = ", q3)
#print("q4 = ", q4)

solution = q1 * q2 * q3 * q4

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
