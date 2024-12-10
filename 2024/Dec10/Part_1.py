# AoC 2024
# Dec10
# Part 1

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

# Functions from Dec04
def find_char(s: str, ch: chr):
    return [idx for idx, letter in enumerate(s) if letter == ch]

def neighbors(letter_list: list, next_letter_list: list):
    N_list = []
    W_list = []
    E_list = []
    S_list = []
    for letter in letter_list:
        n_ = (letter[0]-1, letter[1])
        w_ = (letter[0], letter[1]-1)
        e_ = (letter[0], letter[1]+1)
        s_ = (letter[0]+1, letter[1])

        if n_ in next_letter_list:
            N_list.append(n_)
        if w_ in next_letter_list:
            W_list.append(w_)
        if e_ in next_letter_list:
            E_list.append(e_)
        if s_ in next_letter_list:
            S_list.append(s_)
        
        rDict = {"N" : N_list,
                 "W" : W_list,
                 "E" : E_list,
                 "S" : S_list,
                 }
        
    return rDict

# Fill dictionary with location coordiantes for digits
tmp_list = []
digit_locations = {}
for digit in range(10):
    tmp_list.clear()
    for row_num in range(len(data)):
        tmp_list.extend([(row_num, idx) for idx in find_char(data[row_num], str(digit))])
    digit_locations[str(digit)] = tmp_list.copy()

#digit_locations.clear()
#digit_locations["0"] = [(0,2)]
#print("digit_locations: ",  digit_locations)
#digit_locations.clear()
#digit_locations["0"] = [(0,2)]


trailheads = {}
trails = []
next_trails = []
#trailhead_score = 0
for candidate in digit_locations["0"]:
    #print("candidate = ", candidate)
    trails.clear()
    trails.append([candidate])
    #print("trails = ", trails)
    for digit in range(1,10):
        for trail in trails:
            #print("trail = ", trail)
            trail_length = len(trail)
            #print("trail_length = ", trail_length)
            trail_endpoint = [trail[-1]]
            #print("trail_endpoint = ", trail_endpoint)
            next_neighbors = neighbors(trail_endpoint, digit_locations[str(trail_length)])["N"] \
            + neighbors(trail_endpoint, digit_locations[str(trail_length)])["W"] \
            + neighbors(trail_endpoint, digit_locations[str(trail_length)])["E"] \
            + neighbors(trail_endpoint, digit_locations[str(trail_length)])["S"]
            #print("next_neighbors = ", next_neighbors)
            for neighbor in next_neighbors:
                newtrail = trail + [neighbor]
                if len(newtrail) >= 10:
                    #print("newtrail = ", newtrail)
                    #trailheads[tuple(newtrail)] = "10"
                    trailheads[(candidate,neighbor)] = 1
                else:
                    next_trails.append(newtrail)
                
                #print("next_trails = ", next_trails)
                
        trails = next_trails.copy()
        next_trails.clear()

#print("trailheads = ", trailheads)
#for the_key in trailheads.keys():
#    print(the_key)

solution = len(trailheads)
print("Solution: ", solution)

