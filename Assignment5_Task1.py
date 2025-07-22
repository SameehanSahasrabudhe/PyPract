# Assignment 5 

# Task 1: Create a Dictionary of Student Marks

marks = {'Sam':99, 'Mark':84, 'John':90, 'Stephen':87, 'Akash':92}

Student_name = input('Enter the student\'s name : ')

if Student_name in marks.keys():
    print(Student_name +'\'s marks:', marks[Student_name])
else:
    print("Student name not found, please enter correct student name.") 

