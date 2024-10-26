# from curses.ascii import isalpha
from itertools import count

#1.1
# user_list=list(input('Enter string:').lower())
# print(user_list)


# 1.2
#
# user_list=[('p', 2), ('u', 1), ('l', 1), ('' , 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
#
#
# vowels='aueioy'
#
# list_vow=[(char,count) for char,count in user_list if char in vowels and char.isalpha()]
# list_cons=[(char,count) for char,count in user_list if char not in vowels and char.isalpha()]
# list_sym=[(char,count) for char,count in user_list if not char.isalpha()]
#
#
# print('Дауысты:',list_vow)
# print('Дауыссыз:',list_cons)
# print('Символдар:',list_sym)

# 2.1
# name=input('Student name - ')
# assignments =input('scores for assignments = ').split(',')
# labs=input('labs= ').split(',')
# tests =input('tests= ').split(',')
#
# student={
# 'name':name,
# 'assignment':assignments,
# 'test':tests,
# 'lab':labs
# }
#
# print(student)
#
# # 2.2
# count=len(student['assignment'])+len(student['test'])+len(student['lab'])
#
# task={
#     student['name']:count
# }
#
# print(task)