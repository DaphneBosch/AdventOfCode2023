# # Puzzle 1: Trebuchet
import re

# Prepare a word list to find the words that are written out in the day1_txt file
number_list = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Set the sum list to zero
sum_list = 0


# Function to search the list

# This code is used for part one
# def search_list(list_line):
#     for word, number in number_list.items():
#         list_line = list_line.replace(number, word + number + word)
#     return list_line

# This code is used for part two
def search_list(list_line):
    for word, number in number_list.items():
        list_line = list_line.replace(word, word + number + word)
    return list_line


# Open the day1_calibration.txt file use a for loop and print the number found on the line
with open('input/day1_calibration.txt', 'r') as file:
    # Read the lines in the file
    line_in_list = file.readlines()

    # Loop through the file in order to find the first and last number
    for lines in line_in_list:
        # Remove the whitespace from a line
        lines = lines.strip()

        # Search the line in the list
        line_sec = search_list(lines)

        # Search for the first number in a line
        search_first = re.search(r'\d', line_sec)
        first_num = search_first.group()
        reverse = line_sec[::-1]

        # Search for the last number in a line
        search_last = re.search(r'\d', reverse)
        last_num = search_last.group()

        # Combine the numbers together
        number = first_num + last_num

        # Print the number per line
        print(f"Number on this line: {number}")
        sum_list += int(number)

# Sum of the numbers is displayed here
print(f"Sum of list: {sum_list}")
