# AoC 2025
# Dec 2
# Part 2
import datetime
import re
import os

start_time = datetime.datetime.now()

# Import today's data
basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
print(dirname)
print(basename)
#data = [l.strip() for l in open(dirname + "/Input/example.txt", "rt")]
data = [l.strip() for l in open(dirname + "/Input/input.txt", "rt")]
print(data)
print("----------------")

def find_repeated_patterns(id: int):
    id_text = str(id)
    id_length = len(id_text)
    for pattern_length in range(1, id_length // 2 + 1):
        if id_length % pattern_length == 0:
            pattern = id_text[:pattern_length]
            #print(pattern)
            match_indices = [match.start() for match in re.finditer(pattern, id_text)]
            if len(match_indices) * pattern_length == id_length:
                return id
    return 0

interval_list = data[0].split(",")
#print(interval_list)

sum_bogus_ids = 0
for interval in interval_list:
    for check_id in range(int(interval.split("-")[0]), int(interval.split("-")[1]) + 1):
        #print(check_id)
        bogus_id = find_repeated_patterns(check_id)
        sum_bogus_ids = sum_bogus_ids + bogus_id

#print(sum_bogus_ids)
solution = sum_bogus_ids


#x = find_repeated_patterns(123123)
#print(x)
#x = find_repeated_patterns(123123123)
#print(x)
#x = find_repeated_patterns(1231231234)
#print(x)

#solution = None # Assign value of solution

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
