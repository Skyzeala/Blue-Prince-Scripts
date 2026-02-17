# This script will display all permutations of letters given

import itertools
import time 

input_string = input("String: ").strip()
letter_list = list(input_string)

if len(letter_list) > 15:
    print("Input too long, too many results. Try something with less than 8 characters.")
    exit()

if len(letter_list) > 8:
    print("Input is very long, are you prepared for 1 million results?")
    time.sleep(5)

perm_iter = itertools.permutations(letter_list)

for perm in perm_iter:
    print("".join(perm))
