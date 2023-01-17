def menu():
    print("1. CGPA of one Semester")
    print("2. CGPA of Multiple Semesters")
    return int(input("Enter Your Choice:  "))


name = input("Enter Your Name:  ")
choice = menu()
if choice == 1:
    semester = input("Current Semester: ")
    totalCreditHours = 0
    courses = int(input("No. of Courses:  "))
    gpa = []
    creditHours = []
    cgpa = 0

    for i in range(courses):
        creditHours.append(int(input(f"Enter the Credit Hours of Subject {i+1}:  ")))
        gpa.append(float(input(f"Enter the GPA of Subject {i+1}:  ")))
        totalCreditHours = totalCreditHours + creditHours[i]
        cgpa = cgpa + gpa[i]/creditHours[i]

    cgpa = cgpa / courses
    print(f"Total Credit Hours:  {totalCreditHours}")
    print(f"CGPA of {name} in {semester} semester is:  {round(cgpa,2)}")

elif choice == 2:
    totalSemesters = int(input("Enter the No. of Semesters:  "))
    gpa = []
    cgpa = 0
    for i in range(totalSemesters):
        gpa.append(float(input(f"Enter the CGPA of semester {i+1}: ")))
        cgpa += gpa[i]

    cgpa = cgpa / totalSemesters
    print(f"CGPA of {name} in {totalSemesters} semesters is:  {round(cgpa,2)}")

else:
    print("Invalid Operation.")

