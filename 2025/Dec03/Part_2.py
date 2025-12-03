# AoC 2025
# Dec 3
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

def max_joltage(digits_list: list, number_of_digits: int):
    if len(digits_list) <= number_of_digits:
        return digits_list
    
    max_digit = max(digits_list)
    count_max_digit = digits_list.count(max_digit)
    if count_max_digit >= number_of_digits:
        return [max_digit for dummy in range(number_of_digits)]
    
    index_max_digit = digits_list.index(max_digit)
    if index_max_digit <= len(digits_list) - number_of_digits:
        # The highest digit can be the first digit in the voltage
        return [max_digit] + max_joltage(digits_list[index_max_digit + 1:], number_of_digits - 1)
    else:
        # The highest digit can't be the first digit in the voltage, so we want it as far to the left as possible
        return max_joltage(digits_list[:index_max_digit], number_of_digits - len(digits_list[index_max_digit:])) + digits_list[index_max_digit:]


joltage_sum = 0
for battery_bank in data:
    battery_bank_list = [int(battery) for battery in battery_bank]
    joltage = max_joltage(battery_bank_list, 12)
    joltage_text = "".join(map(str, joltage))
    joltage_num = int(joltage_text)
    joltage_sum = joltage_sum + joltage_num


solution = joltage_sum # Assign value of solution

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
