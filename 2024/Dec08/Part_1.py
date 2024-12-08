# AoC 2024
# Dec08
# Part 1

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

def find_antinode(antenna1: tuple, antenna2:tuple, rows, cols):
    dist = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
    outer_antinode1 = (antenna1[0] - dist[0], antenna1[1] - dist[1])
    outer_antinode2 = (antenna2[0] + dist[0], antenna2[1] + dist[1])
    if dist[0]%3 == 0 and dist[1]%3 == 0:
        inner_antinode1 = (antenna1[0] + dist[0]//3, antenna1[1] + dist[1]//3)
        inner_antinode2 = (antenna2[0] - dist[0]//3, antenna2[1] - dist[1]//3)
    else:
        inner_antinode1 = (-1, -1)
        inner_antinode2 = (-1, -1)
    
    antinode_list = []

    if outer_antinode1[0] >= 0 and outer_antinode1[0] < rows and outer_antinode1[1] >= 0 and outer_antinode1[1] < cols:
        antinode_list.append(outer_antinode1)
    if outer_antinode2[0] >= 0 and outer_antinode2[0] < rows and outer_antinode2[1] >= 0 and outer_antinode2[1] < cols:
        antinode_list.append(outer_antinode2)
    if inner_antinode1[0] >= 0 and inner_antinode1[0] < rows and inner_antinode1[1] >= 0 and inner_antinode1[1] < cols:
        antinode_list.append(inner_antinode1)
    if inner_antinode2[0] >= 0 and inner_antinode2[0] < rows and inner_antinode2[1] >= 0 and inner_antinode2[1] < cols:
        antinode_list.append(inner_antinode2)

    #print(dist)
    #print(outer_antinode1)
    #print(outer_antinode2)
    #print(inner_antinode1)
    #print(inner_antinode2)

    return antinode_list
    
#find_antinode((8, 8), (5, 6), 12, 12)
#find_antinode((5, 6), (8, 8), 12, 12)
#find_antinode((3, 7), (4, 4), 12, 12)
#find_antinode((4, 4), (3, 7), 12, 12)

#find_antinode((2, 3), (5, 3), 8, 8)
#find_antinode((5, 3), (2, 3), 8, 8)

#antinodes = find_antinode((0, 3), (6, 0), 8, 8)
#print(antinodes)
#antinodes = find_antinode((6, 0), (0, 3), 8, 8)
#print(antinodes)
#antinodes = find_antinode((0, 0), (6, 3), 8, 8)
#print(antinodes)

#print(" result: " + str(_result))
    

# Find antennas
rows = len(data)
cols = len(data[0]) 
print("rows: " + str(rows))
print("cols: " + str(cols))

antenna_count = {}
antenna_list = []
for row in data:
    antenna_list.extend([char for char in list(row) if char != '.' and char != '#'])
for antenna in antenna_list:
    antenna_count[antenna] = antenna_count.get(antenna, 0) + 1

#print(antenna_list)
#print(antenna_count)

antenna_row_col = {}
antenna_coordinates = {}
for row_num in range(rows):
    for col_num in range(cols):
        pos_char = data[row_num][col_num]
        if pos_char != '.' and pos_char != '#':
            antenna_row_col[(row_num, col_num)] = data[row_num][col_num]
            antenna_coordinates[pos_char] = antenna_coordinates.get(pos_char, []) + [(row_num, col_num)]
#print('--------------')
#print(antenna_row_col)
print("------------------")
print("antenna_coordinates:")
print(antenna_coordinates)

antenna_pairs = []
for antenna_type in antenna_coordinates.keys():
    for antenna1_idx in range(len(antenna_coordinates[antenna_type])):
        for antenna2_idx in range(antenna1_idx+1, len(antenna_coordinates[antenna_type])):
            antenna_pairs.append((antenna_coordinates[antenna_type][antenna1_idx], (antenna_coordinates[antenna_type][antenna2_idx])))

#print(antenna_pairs)

antinodes = {}
for antenna_pair in antenna_pairs:
    antinodes_list = find_antinode(antenna_pair[0], antenna_pair[1], rows, cols)
    for antinode_xy in antinodes_list:
        antinodes[antinode_xy] = antinodes.get(antinode_xy, 0) + 1

print("------------------")
print("antinodes:")
print(antinodes)
print("Antinodes: " + str(len(antinodes)))
