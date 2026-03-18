#cout number of students

num_of_students=int(input("Enter the no of students: "))

#store student data
StudentData = []#list

for i in range(num_of_students):
    print(f"Enter the Data of Student {i+1}")
    name = input("name: ")
    roll_no = int(input("Roll no: "))
    marks =int(input("Marks: "))

    if marks > 90:
        grades="A"
    elif marks>80:
        grades="B"
    elif marks >70:
        grades="C"
    elif marks >60:
        grades="D"
    elif marks >=33:
        grades="E"
    else:
        grades = "F"
    
    students={
        "name":name,
        "Roll no":roll_no,
        "marks": marks,
        "grades":grades
        }
    StudentData.append(students)

#Data printing

print("All student data are: \n")

for s in StudentData:
    print(f"Name: {s['name']}- Roll No: {s['Roll no']}- Marks: {s['marks']}- Grade: {s['grades']}")


print("Student who are passed")
for s in StudentData:
    if s['marks'] >= 33:
        print(f"{s['name']}-{s['marks']}")
  