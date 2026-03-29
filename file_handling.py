import csv

# Writing to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    for i in range(3):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        writer.writerow([name, marks])

# Reading from CSV
print("\nReading student data:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)