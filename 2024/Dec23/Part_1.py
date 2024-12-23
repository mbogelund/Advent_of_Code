# AoC 2024
# Dec 23
# Part 1
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

#print(k3_computers)

t_k3 = [k3_key for k3_key in list(k3_computers.keys()) if k3_computers[k3_key] > 0]
#print(t_k3)

solution = len(t_k3)

#print(connections)
#print(connected)

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
