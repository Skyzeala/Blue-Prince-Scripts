# This script will convert a string to numbers and back again using a1z26 cipher
# Number results are comma separated and non alpha characters will not be changed

to_num = input("Convert text to numbers? (t/f): ")
to_num = ("t" == to_num or "T" == to_num)
in_string = input("Please enter the text/numbers to convert: ")

output_list = []

if (to_num):
    for letter in in_string:
        out_num = ord(letter)
        
        if out_num > 96 and out_num <= 96+26:
            out_num -= 96
        elif out_num > 64 and out_num <= 64+26:
            out_num -= 64
        else:
            output_list.append(letter + ",")
            continue
        
        output_list.append(str(out_num) + ",")
else:
    num_list = in_string.split(",")

    for num in num_list:
        if not(num.isdigit()):
            output_list.append(num)
            continue
        out_letter = chr(int(num)+64)
        output_list.append(out_letter)

#print("output list: ", output_list)
print("output string: ", "".join(output_list))
