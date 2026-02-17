# This script contains major spoilers for late game puzzles

# This script will find the numeric core of 4 ordered numbers
# If the result is over 1000, run the script again with the new digits

smallest_whole = 10000

number_input = input("Please enter 4 non-zero numbers separated by commas: ")

number_input = number_input.split(",")
number_list = []
for number in number_input:
    number_list.append(int(number.strip()))

print(number_list)

testing_value = ((number_list[0] - number_list[1]) * number_list[2]) / number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

testing_value = ((number_list[0] - number_list[1]) / number_list[2]) * number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

testing_value = ((number_list[0] * number_list[1]) / number_list[2]) - number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

testing_value = ((number_list[0] * number_list[1]) - number_list[2]) / number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

testing_value = ((number_list[0] / number_list[1]) * number_list[2]) - number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

testing_value = ((number_list[0] / number_list[1]) - number_list[2]) * number_list[3]
#print(testing_value)
if (testing_value > 0 and testing_value.is_integer() and testing_value < smallest_whole):
    smallest_whole = testing_value

if (smallest_whole == 10000):
    smallest_whole = "Could not find numeric core"

print("Result = ", smallest_whole)