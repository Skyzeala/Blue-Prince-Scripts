# This script can evaluate a math problem using an input string
# This script does not check the validity of the input

import operator
import math

print("Letters signify the colors of the numbers that follow them")
print("\tc = cyan/blue (addition)\n",
      "\ty = yellow (subtraction)\n",
      "\tm = magenta/pink (multiplication)\n",
      "\tp = purple (division)\n")
print("Dart board functions can also be used, these should appear after the number")
print("\t** = Perform the last operation twice\n",
      "\t*** = Perform the last operation three times\n",
      "\t**** = Perform the last operation four times\n",
      "\tx = Skip the last operation\n",
      "\t/ = half the last number\n",
      "\t\\ = third the last number\n")
print("Algebra symbols appear after the number and dart board symbols (except x)")
print("\t[] = square (actually only checks for ])\n",
      "\t<> = reverse/inverse (actually only checks for >)\n",
      "\t~ = round to nearest whole\n",
      "\t~~ = round to nearest tens\n",
      "\t~~~ = round to nearest hundreds\n")

in_string = input("Math problem: ") + " "

curr_num = 0
next_result = 0
round_digit = 0 
num_of_times = 0
last_num = 0
op_function = operator.add
last_letter = "c"

for letter in in_string:
    last_letter = letter
    if curr_num.is_integer():
        curr_num = int(curr_num)
    if next_result.is_integer():
        next_result = int(next_result)

    if round_digit < 0 and letter != "~":
        if (next_result - int(next_result) >= 0.49): #prevent floating point errors
            next_result = math.ceil(next_result)
        next_result = round(next_result, round_digit+1)
        round_digit = 0
    if num_of_times > 0 and letter != "*":
        next_result = curr_num
        while num_of_times > 0:
            next_result = op_function(next_result, last_num)
            num_of_times -= 1
    if letter.isalpha(): #perform the last operation and prepare for the next
        if letter == "x":
            next_result = curr_num
        if letter == "c" or letter == "b":
            op_function = operator.add
        if letter == "y":
            op_function = operator.sub
        if letter == "m":
            op_function = operator.mul
        if letter == "p":
            op_function = operator.truediv
        curr_num = next_result
        last_num = 0
        decimal_place = 0
    if letter.isdigit():
        if decimal_place < 1:
            last_num = last_num * 10 + int(letter)
        else:
            last_num = last_num + (int(letter) / pow(10, decimal_place))
            decimal_place +=1
        next_result = op_function(curr_num, last_num)
    if letter == ".":
        decimal_place = 1
    elif letter == "/":
        last_num /= 2
        next_result = op_function(curr_num, last_num)
    elif letter == "\\":
        last_num /= 3
        next_result = op_function(curr_num, last_num)
    elif letter == "~":
        round_digit -= 1
    elif letter == "*":
        num_of_times += 1
    elif letter == "]":
        next_result *= next_result
    elif letter == ">": #cannot handle negative numbers at the moment
        if next_result.is_integer():
            next_result = int(next_result)
        next_result = float(str(next_result)[::-1])
    else: #ignore unrecognized symbols like spaces and parentheses
        continue

curr_num = next_result

print(curr_num)