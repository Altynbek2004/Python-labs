
# 1.1
# user_list=list(input('Enter string:').lower())
# print(user_list)
#
#
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

# # 2.1
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
# count_submission=len(student['assignment'])+len(student['test'])+len(student['lab'])
#
# submission_rate={
#     student['name']:count_submission
# }
#
# print(submission_rate)

# 2.3

# def average(tasks):
#     all_final=0
#     for task in tasks:
#         all_final+=float(task)
#     return all_final/len(tasks) if tasks else 0
#
#
#
#
# if submission_rate[student['name']]>=4:
#     final_grade=0.3*average(student['assignment'])+0.5*average(student['lab'])+0.2*average(student['test'])
#     student['final_grade']= final_grade
#     print(student)
# else:
#     student['final_grade']=0
#     print(student)

# 2.4

# student2={
#     'name': 'Kevin',
#     'assignment': [82, 30],
#     'test': [],
#     'lab': [78.2]
# }
#
# student_name1=student['name']
# student_name2=student2['name']
# del student['name']
# del student2['name']
# students={
#     student_name1:student,
#     student_name2:student2
# }
#
# print(students)