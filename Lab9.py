
# Task 1
# There is a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Print all the elements that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for item in a:
#     if item<5:
#         print(item)


# Task 2
# The lists are given:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# You need to return a list that consists of elements that are common to these two lists.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# c=[]
# for itemA in a:
#     for itemB in b:
#         if itemA==itemB and itemA not in c:
#             c.append(itemA)
#
# print(c)

# final_list=list(set(a)&set(b))
# print(final_list)


# Task 3
# Sort the dictionary by value in ascending and descending order.

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d_asc=dict(sorted(d.items(),key=operator.value(1)))
# sorted_d_desc=dict(sorted(d.items(),key=operator.value(1),reverse=True))
#
# print(sorted_d_asc)
# print(sorted_d_desc)


#Task 4
# Write a program to merge several dictionaries into one.
# Let's say here are our dictionaries:

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
#
# merged_dict = {}
# for d in (dict_a, dict_b, dict_c):
#     merged_dict.update(d)
#
# print(merged_dict)

# Task 5
# Find the three keys with the highest values in the dictionary
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# highest_values = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# print(highest_values)



# Task 6
# Write a code that converts an integer into a string, despite the fact that it can be used in any number system.

# def int_to_base(san, negiz):
#     if san == 0:
#         return "0"
#     elif negiz < 2 or negiz > 36:
#         raise ValueError("Сандық негіз 2 мен 36 арасында болу керек")
#
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ""
#     is_negative = san < 0
#     san = abs(san)
#
#     while san > 0:
#         qaldyq = san % negiz
#         result = digits[qaldyq] + result
#         san //= negiz
#
#     if is_negative:
#         result = "-" + result
#
#     return result
#
# mani=int_to_base(45,2)
# print(mani)

# Task 7
# You need to print the first n lines of Pascal's triangle. In this triangle, there are units at the top and on the sides, and each number inside is equal to the sum of the two numbers above it.
#
# def print_pascals_triangle(n):
#     triangle = []
#
#     for i in range(n):
#
#         row = [1] * (i + 1)
#
#         for j in range(1, i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#
#     for row in triangle:
#         print(" " * (n - len(row)), " ".join(map(str, row)))
#
#
#
# print_pascals_triangle(5)





#
#
#
#
# n=int(input('Enter n:'))
# triangle=[]
#
# for i in range(n):
#     row=[1]*(i+1)
#
#     for j in range(1,i):
#         row[j]=triangle[i-1][j-1]+triangle[i-1][j]
#
#     triangle.append(row)
#
# for i in range(1,2):
#    print(i)
#
# for t in triangle:
#  print(t)




# a=str(input("Enter a:"))
# b=int(input("Enter b:"))
#
# y=int (a,b)
# print(y)