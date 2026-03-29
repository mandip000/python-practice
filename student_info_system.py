import csv

def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, marks])

def search_student():
    name = input("Enter name to search: ")
    found = False
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print("Found:", row)
                found = True
                break
    if not found:
        print("Student not found.")

while True:
    print("\n1. Add student\n2. Search student\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        break
    else:
        print("Invalid choice")