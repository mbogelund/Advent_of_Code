# AoC 2024
# Dec 23
# Part 2
import datetime
import re

start_time = datetime.datetime.now()

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

connected = {}
connections = {}
for row in data:
    computers = row.split("-")
    connections[(computers[0], computers[1])] = len([t_comp for t_comp in computers if t_comp[0] == "t"])
    connections[(computers[1], computers[0])] = len([t_comp for t_comp in computers if t_comp[0] == "t"])
    connected[computers[0]] = list(dict.fromkeys(connected.get(computers[0], []) + [computers[1]]))
    connected[computers[1]] = list(dict.fromkeys(connected.get(computers[1], []) + [computers[0]]))

all_computers = sorted(list(connected.keys()))
k3_computers = {}
for computer1_idx in range(len(all_computers)):
    computer1 = all_computers[computer1_idx]
    #print(computer1)
    for computer2_idx in range(computer1_idx + 1, ):
        computer2 = all_computers[computer2_idx]
        comp1_comp2 = (computer1, computer2)
        comp1_comp2_connected = connections.get(comp1_comp2, None)
        #print(" ", computer2)
        if comp1_comp2_connected is not None:
            #print(comp1_comp2)
            for computer3_idx in range(computer2_idx + 1, ):
                computer3 = all_computers[computer3_idx]
                comp1_comp3 = (computer1, computer3)
                comp2_comp3 = (computer2, computer3)
                comp1_comp3_connected = connections.get(comp1_comp3, None)
                comp2_comp3_connected = connections.get(comp2_comp3, None)
                #print("  ", computer3)
                if comp1_comp3_connected is not None and comp2_comp3_connected is not None:
                   k3 = (computer1, computer2, computer3)
                   k3_computers[k3] = len([t_comp for t_comp in k3 if t_comp[0] == "t"])


# OK, nice! We weren't supposed to only look at complete sub-networks containing a t-computer...
#t_k3 = [tuple(sorted(k3_key)) for k3_key in list(k3_computers.keys()) if k3_computers[k3_key] > 0]
t_k3 = [tuple(sorted(k3_key)) for k3_key in list(k3_computers.keys())]

complete_candidates = set(t_k3)
new_complete_candidates = set()

while len(complete_candidates) > 0:
    K_subgraph = complete_candidates.pop()
    investigate = set()
    for computer in K_subgraph:
        investigate = investigate.union(set(connected[computer]))
    for computer in K_subgraph:
        investigate.remove(computer)
    while len(investigate) > 0:
        candidate = investigate.pop()
        possible_candidate = True
        for computer in K_subgraph:
            if possible_candidate:
                if connections.get((computer, candidate), None) == None:
                    possible_candidate = False
        if possible_candidate:
            new_complete_candidates.add(tuple(sorted((list(K_subgraph)) + [candidate])))
    if len(complete_candidates) == 0:
        if len(new_complete_candidates) > 0:
            largest_complete_subgraphs = new_complete_candidates.copy()
            complete_candidates.update(new_complete_candidates)
            new_complete_candidates.clear()
        else:
            print("Largest complete subgraph(s):")
            for subgraph in largest_complete_subgraphs:
                print(subgraph)

#value_sorted_connected = sorted(connected.items(), key=lambda x:len(x[1]))

solution = ",".join(list(largest_complete_subgraphs.pop()))


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
