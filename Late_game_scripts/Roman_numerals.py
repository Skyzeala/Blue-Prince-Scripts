# This script can convert to and from roman numerals

roman_dict = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

convert_to_roman = input("Convert int to roman? (y/n): ")
convert_to_roman = convert_to_roman == "y"

input_string = input("Enter your number: ")
input_string = input_string.strip()

if input_string == "0":
    print("No roman numeral found")
    exit()

output_list = []
output_num = 0

if convert_to_roman:
    input_num = int(input_string)
    for numeral in roman_dict:
        num_str = numeral*(input_num // roman_dict[numeral])
        if num_str != '':
            output_list.append(num_str)
            input_num = input_num % roman_dict[numeral]
else: #convert to arabic numbers
    input_string = input_string.upper()
    for numeral in roman_dict:
        while input_string.startswith(numeral):
            output_num += roman_dict[numeral]
            input_string = input_string[len(numeral):]
    output_list.append(str(output_num))

print("".join(output_list))
