students = {}
for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

def average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

print("Student Marks:", students)
print("Average Marks:", average(students))