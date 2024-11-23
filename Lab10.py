# Task 1
# Write a check to see if the string is a palindrome. A palindrome is a word or phrase that reads equally from left to right and from right to left.


# x=input('Кез келген сөз енгізіңіз: ').lower()
# if x==x[::-1]:
#     print('Палиндром')
# else:
#     print('Палиндром емес')


# Task 2
# Make the number of seconds appear as days:hours:minutes:seconds.
# seconds = int(input("Уақытты секундпен енгізіңіз: "))
# days = seconds // 86400
# seconds %= 86400
# hours = seconds // 3600
# seconds %= 3600
# minutes = seconds // 60
# seconds %= 60
#
# print("Күн:сағат:минут:секунд:",f"{days}:{hours:02}:{minutes:02}:{seconds:02}")


# Task 3
# You accept from the user a sequence of numbers separated by a comma. Make a list and a tuple with these numbers.


# numbers = input("Сандарды үтір арқылы енгізіңіз: ")
#
# numbers_list = numbers.split(",")
# numbers_tuple = tuple(numbers_list)
#
# print("List:", numbers_list)
# print("Tuple:", numbers_tuple)


# Task 4
# Print the first and last item in the list.

# items = input("List элементтерін үтірмен енгізіңіз: ").split(",")
#
#
# if items:
#     print("1-ші элемент:", items[0])
#     print("2-ші элемент:", items[-1])
# else:
#     print("List бос!")


# Task 5
# Write a program that accepts the file name and outputs its extension. If the file extension cannot be determined, throw an exception.

# file_name = input("Файл атын енгізіңіз: ")
# try:
#     if "." in file_name and file_name.rsplit(".", 1)[1]:
#         print(file_name.rsplit(".", 1)[1])
#     else:
#         raise ValueError("Файл кеңейтімі анықталмады.")
# except Exception as e:
#     print(e)



# Task 6
# For a given integer n, count n + nn + nnn.

# n = int(input("Сан енгізіңіз: "))
# result = int(n) + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))
# print("Жауабы:", result)


# Task 7
# Write a program that outputs even numbers from a given list and stops if it encounters the number 237.

# user_input = input("Сандар тізбегін үтір арқылы енгізіңіз: ")
# numbers_list = list(map(int, user_input.split(",")))
#
# for number in numbers_list:
#     if number == 237:
#         print(number)
#         break
#     if number % 2 == 0:
#         print(number)

