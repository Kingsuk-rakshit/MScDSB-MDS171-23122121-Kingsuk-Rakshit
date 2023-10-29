# # Create a menu driven program that collects students data :
# # > Name, Reg_No, Email & Phone
# # [Use dictionary to store student details]

# # Menu Options
# # 1. Create Students
# # 2. Search for students
# # 3. Print Students

# stu_details = {}

# # Store students details :
# def create_student(name, reg_no, email, phone):
#     student = {
#         'Name' : name,
#         'Email' : email,
#         'Phone' : phone,
#     }
#     stu_details[reg_no] = student
#     if student in stu_details:
#         return False
#     else:
#         student.append(stu_details)
#         return True

# # Collect user input
# def collect_student_info():
#     name = input("Enter Student Name: ")
#     reg_no = input("Enter Student Reg_No: ")
#     email = input("Enter Student Email: ")
#     phone = input("Enter Student Phone: ")
#     return name, reg_no, email, phone

# # Print Students
# def print_students():
#     for reg_no in stu_details.keys():
#         print(reg_no, end="\t")
#         for key in stu_details[reg_no]:
#             print(stu_details[reg_no][key],end='\t')
#         print()

# while True:
#     print("Menu options")
#     print("*"*30)
#     print("1. Enter Student Info ")
#     print("2. List students ")
#     print("3. Exit ")

#     choice = input("Enter the choice").strip()
#     if choice == "1":
#         name, regno, email, phone = collect_student_info()
#         create_student(name, regno, email, phone)
#     elif choice == "2":
#         print_students()
#     elif choice == "3":
#         exit()
#     else:
#         print("Invalid Choice")






# Create a menu driven program that collects students details
# > Name, Register Number, Email & Phone
# [Use dictionary to store student details]

# Menu Options
# 1. Create Students
# 2. Search for Students
# 3. Print Students

studentDict = {}

def createStudent(name,regno,email,phone):
    student = {
        "Name": name,
        "Email": email,
        "Phone": phone
    }

    studentDict[regno] = student

def colletStudentInfo():
    name = input("Enter Student Name: ")
    regno = input("Enter Student regno: ")
    email = input("Enter Student Email: ")
    phone = input("Enter Student Phone: ")
    return name, regno, email, phone

def printStudents():
    print("Regno\tName\tEmail\tPhone")
    for regno in studentDict.keys():
        print(regno,end="\t")
        for key in studentDict[regno]:
            print(studentDict[regno][key],end='\t')
        print()

while True:
    print("Menu Options")
    print("1. Enter Student Info")
    print("2. List Students")
    print("3. Exit")

    choice = input("Enter the choice").strip()
    if choice == "1":
        name, regno, email, phone = colletStudentInfo()
        createStudent(name, regno, email, phone)
    elif choice == "2":
        printStudents()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
    