# 1. Write a python Program that uses class to store the name and marks in 4 subjects of students. Use 
# the list to store the marks in 4 subjects. 
# Also find the total marks of the students and find the name of the students who have obtained the 
# highest total marks.

# student class
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def calculate_total(self):
        total=0
        for i in self.marks:
            total+=i
        return total

# calculate highest marks
def calculate_highest_marks(student_list):
    print(f"----------------Total marks of student-------------------")
    highest=0
    for student in student_list:
        print(f"Student name - {student.name}\tTotal marks - {student.calculate_total()}")
        if student.calculate_total() >= highest:
            highest=student.calculate_total()
            student_name=student.name
    print(f"---------------------------------------------------------")
    print(f"Highest marks - {highest} and student name - {student_name}")

# main code 
student_list=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input(f"Enter the name of student {i + 1}: ")
    marks_list=[]
    for j in range(4):
        marks=float(input(f"Enter marks for subject {j + 1}: "))
        marks_list.append(marks)
    student=Student(name,marks_list)
    student_list.append(student)
# function call
calculate_highest_marks(student_list)