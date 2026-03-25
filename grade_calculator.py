print("Student Grade Calculator")

# Input marks
math = float(input("Enter marks for Math: "))
physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))

# Calculate total and average
total = math + physics + chemistry
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)

# Assign grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)