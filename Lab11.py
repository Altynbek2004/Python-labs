# Task 1
# Write a program that accepts two lists and outputs all the elements of the first one that are not in the second one.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
#
# for item in list1:
#     if item not in list2:
#         print(item)


# Task 2
# Print a list of files in the specified directory.
#
# import os
# directory = "C:/Users/дл.DESKTOP-N32060M/Pictures/Screenshots"
# for file in os.listdir(directory):
#     print(file)


# Task 3
# number =648
# sum_of_digits = 0
#
# for digit in str(number):
#     sum_of_digits += int(digit)
#
# print(sum_of_digits)


# Task 4
# Count the number of times a character occurs in a string.
string = "Altynbekaaaaaaaaaaaa"
char = "a"
count = string.count(char)
print(count)

# Task 5
# Swap the values of the variables.
#
# a = 5
# b = 10
#
# a, b = b, a
# print(a, b)

# Task 6
# Use the anonymous function to extract numbers divisible by 15 from the list.
#
# numbers = [1, 2, 3, 15, 30, 45]
#
# result = filter(lambda x: x % 15 == 0, numbers)
# for number in result:
#     print(number)

# Task 7
# You need to check if all the numbers in the sequence are unique.
# numbers = [1, 2, 3, 4, 5]
#
# if len(numbers) == len(set(numbers)):
#     print("Барлық сандар қайталанбайды.")
# else:
#     print("Қайталанатын сандар бар.")
