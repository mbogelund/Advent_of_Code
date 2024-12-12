# AoC 2024
# Dec12
# Part 1
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

rows = len(data)
cols = len(data[0])

def same_region(focus_plot: tuple, focus_letter: str):
    return_list = []
    #focus_letter = plot_dict[focus_plot]
    if plot_dict.get((focus_plot[0] - 1, focus_plot[1]), "_") == focus_letter:
        return_list.append((focus_plot[0] - 1, focus_plot[1]))
    if plot_dict.get((focus_plot[0] + 1, focus_plot[1]), "_") == focus_letter:
        return_list.append((focus_plot[0] + 1, focus_plot[1]))
    if plot_dict.get((focus_plot[0], focus_plot[1] - 1), "_") == focus_letter:
        return_list.append((focus_plot[0], focus_plot[1] - 1))
    if plot_dict.get((focus_plot[0], focus_plot[1] + 1), "_") == focus_letter:
        return_list.append((focus_plot[0], focus_plot[1] + 1))
    return return_list


def fence_count(plot_list: list, rows: int, cols: int):
    count = 0
    for plot in plot_list:
        if (plot[0], plot[1] - 1) not in plot_list:
            count += 1
        if (plot[0], plot[1] + 1) not in plot_list:
            count += 1
        if (plot[0] - 1, plot[1]) not in plot_list:
            count += 1
        if (plot[0] + 1, plot[1]) not in plot_list:
            count += 1
    return count
        

plot_dict = {}
letter_dict = {}
for row in range(len(data)):
    for col in range(len(data[row])):
        plot_dict[(row, col)] = data[row][col]
        letter_xy = letter_dict.get(data[row][col], [])
        letter_xy.append((row, col))
        letter_dict[data[row][col]] = letter_xy.copy()
plot_list = list(plot_dict.keys())
letter_list = list(letter_dict.keys())


region_dict = {}
while len(plot_dict) > 0:
    start_plot = list(plot_dict)[0]
    start_letter = plot_dict[start_plot]
    region_id = (start_plot, start_letter)
    
    #print(region_id)
    region_dict[region_id] = []
    
    investigation_dict = {start_plot: start_letter}
    while len(investigation_dict) > 0:
        investigate_plot = list(investigation_dict)[0]
        letter = investigation_dict.pop(list(investigation_dict)[0])
        region_dict[region_id].append(investigate_plot)
        #print("investigate_plot = ", investigate_plot)
        letter = plot_dict.pop(investigate_plot)
        #print("letter = ", letter)

        for neighbor in same_region(investigate_plot, letter):
            investigation_dict[neighbor] = letter

#print(region_dict)

solution = 0
for region in region_dict:
    solution += fence_count(region_dict[region], rows, cols) * len(region_dict[region])

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
