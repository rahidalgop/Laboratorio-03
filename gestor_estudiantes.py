
# Libraries
# ========================================================================================
import principal

# Variables
# ========================================================================================



students = [{"id":1234, "name":"Ericka", "age":"11", "grade":"5", "subjects":{"Mate":88, "Ingles":90}}, {"id":5678, "name":"Raul", "age":"11", "grade":"5", "subjects":{"Mate":45, "Ingles":25}}]

# Function that displays the login menu

def displayMainMenu ():
    while True:
        print("\n")
        print("========================================================")
        print("STUDENT MANAGEMENT SYSTEM")
        print("========================================================\n")
        print("1. Introduce a new student.")
        print("2. Visualize list of students.")
        print("3. Modify student data.")
        print("4. Delete a student.")
        print("5. Add a new subject.")
        print("6. Grade a subject.")
        print("7. Display report of failed and passed students.")
        print("8. Exit.\n")
        print("========================================================\n")
        mainMenuOption = input("Introduce a number: ")

        mainMenuOption = validateOption(mainMenuOption)

        if mainMenuOption == 1:
            introduceStudent()
        elif mainMenuOption == 2:
            visualizeStudent()
        elif mainMenuOption == 3:
            modifyStudent()
        elif mainMenuOption == 4:
            deleteStudent()
        elif mainMenuOption == 5:
            addSubjectToExisting()
        elif mainMenuOption == 6:
            gradeSubject()
        elif mainMenuOption == 7:
            reports()
        elif mainMenuOption == 8:
            break


# Function that validates that user's input in the menu is correct

def validateOption(option):
    while True:
        try:
            option = int(option)
            if option >= 1 and option <= 8:
                return option
            else:
                print("Invalid argument.")
                option = input("Introduce a valid number: ")
        except ValueError:
            print("Invalid argument.")
            option = input("Introduce a valid number: ")

# Function that creates a new student

def introduceStudent():

    id = input("Introduce the ID of the student: ")
    while True:
        try:
            id = int(id)
            break
        except ValueError:
            print("Invalid argument.")
            id = input("Introduce a valid ID: ")

    name = input("Introduce the name of the student: ")
    
    age = input("Introduce the age of the student: ")
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            print("Invalid argument.")
            age = input("Introduce a valid age: ")

    grade = input("Introduce the grade of the student: ")
    while True:
        try:
            grade = int(grade)
            if grade >= 1 and grade <= 6:
                break
        except ValueError:
            print("Invalid argument.")
            grade = input("Introduce a valid grade (number must be between one and six): ")

    print("Finally, introduce the subjects of the students.")

    newStudent = dict( id = "", name = "", age = "", grade = "", subjects = [] )

    newStudent["id"] = id
    newStudent["name"] = name
    newStudent["age"] = age
    newStudent["grade"] = grade
    newStudent["subjects"] = addSubject()

    students.append(newStudent)

    print(students)
    

# Function that displays the list of students

def visualizeStudent():
    print("\nThis is the current list of students in the system: \n")
    for i in students:
        print(i)


# Function that adds a new calification

def addSubject():
    subjects = {}
    while True:
        subjectName = input("Introduce the name of the subject: ")
        subjectCalification = input("Introduce the calification of the subject: ")
        while True:
            try:
                subjectCalification = int(subjectCalification)
                break
            except ValueError:
                print("Invalid argument.")
                subjectCalification = input("Introduce a valid calification: ")
        option = input("Would you like to add a new subject for this student? (Y/N): ")
        subjects[subjectName] = subjectCalification

        if option.upper() == "N":
            break
    return subjects


# Function that modifies a new student

def modifyStudent():
    indexNumber = 'F'
    id = input("Introduce the ID of the student you want to modify: ")
    while True:
        try:
            id = int(id)
            break
        except ValueError:
            print("Invalid argument.")
            id = input("Introduce a valid ID: ")
    
    for i in range(0, len(students)):
        if id == students[i]["id"]:
            indexNumber = i

    if indexNumber != 'F':
        print("The student was identified. Introduce the value you want to modify.")
        print("\n1. ID.")
        print("2. Name.")
        print("3. Age.")
        print("4. Grade.\n")
        print("========================================================\n")
        modifyOption = input("Introduce a number: ")

        while True:
            try:
                modifyOption = int(modifyOption)
                if modifyOption == 1 or modifyOption == 2 or modifyOption == 3 or modifyOption == 4:
                    break
                else:
                    print("Invalid argument.")
                    modifyOption = input("Introduce a valid number: ")
            except ValueError:
                print("Invalid argument.")
                modifyOption = input("Introduce a valid number: ")

        if modifyOption == 1:
            id = input("Introduce the new ID of the student: ")
            while True:
                try:
                    id = int(id)
                    break
                except ValueError:
                    print("Invalid argument.")
                    id = input("Introduce a valid ID: ")
            students[indexNumber]["id"] = id
            print("The ID was succesfully updated.")

        if modifyOption == 2:
            name = input("Introduce the new name of the student.")
            students[indexNumber]["name"] = name
            print("The name was succesfully updated.")

        if modifyOption == 3:
            age = input("Introduce the new age of the student: ")
            while True:
                try:
                    age = int(age)
                    break
                except ValueError:
                    print("Invalid argument.")
                    age = input("Introduce a valid age: ")
            students[indexNumber]["age"] = age

        if modifyOption == 4:
            grade = input("Introduce the new grade of the student: ")
            while True:
                try:
                    grade = int(grade)
                    if grade >= 1 and grade <= 6:
                        break
                except ValueError:
                    print("Invalid argument.")
                    grade = input("Introduce a valid grade (number must be between one and six): ")
            students[indexNumber]["grade"] = grade
            print("The new grade was succesfully updated.")

    else:
        print("\nThere is not a student registered with the ID you introduced.")

    print(students)


# Function that deletes a student

def deleteStudent():
    indexNumber = 'F'
    id = input("Introduce the ID of the student you want to modify: ")
    while True:
        try:
            id = int(id)
            break
        except ValueError:
            print("Invalid argument.")
            id = input("Introduce a valid ID: ")
    
    for i in range(0, len(students)):
        if id == students[i]["id"]:
            indexNumber = i

    if indexNumber != 'F':
        del students[indexNumber]
    else:
        print("\nThere is not a student registered with the ID you introduced.")

    print(students)


# Function that adds a new subject to an already existing student

def addSubjectToExisting():

    indexNumber = 'F'
    id = input("Introduce the ID of the student you want to modify: ")
    while True:
        try:
            id = int(id)
            break
        except ValueError:
            print("Invalid argument.")
            id = input("Introduce a valid ID: ")
    
    for i in range(0, len(students)):
        if id == students[i]["id"]:
            indexNumber = i

    if indexNumber != 'F':
        print("These are the existing subjects in the student record: \n")
        for i in students[indexNumber]["subjects"]:
            print(i)

        newSubject = input("\nIntroduce the name of the new subject: ")
        students[indexNumber]["subjects"][newSubject] = ""
        print("The new subject was successfully introduced.")
    else:
        print("\nThere is not a student registered with the ID you introduced.")

    print(students)


# Function that adds a new calification to an already existing subject

def gradeSubject():

    indexNumber = 'F'
    id = input("Introduce the ID of the student you want to modify: ")
    while True:
        try:
            id = int(id)
            break
        except ValueError:
            print("Invalid argument.")
            id = input("Introduce a valid ID: ")
    
    for i in range(0, len(students)):
        if id == students[i]["id"]:
            indexNumber = i

    if indexNumber != 'F':
        print("These are the existing subjects in the student record: \n")
        for i in students[indexNumber]["subjects"]:
            print(i)
        
        indexSubject = 'F'

        while True:
            subject = input("\nIntroduce the name of the subject you would like to grade: ")

            if subject in students[indexNumber]["subjects"]:
                newCalification = input("Introduce the new grade of the student: ")
                while True:
                    try:
                        newCalification = int(newCalification)
                        break
                    except ValueError:
                        print("Invalid argument.")
                        newCalification = input("Introduce a valid calification: ")

                students[indexNumber]["subjects"][subject] = newCalification
                print("The new calification was successfully introduced.")
                break
            

            else:
                print("\nThere is not a student registered with the ID you introduced.")

    else:
        print("\nThere is not a student registered with the ID you introduced.")

    print(students)

# Function that displays the report of failed and passed students

def reports():

    approvedStudents = []
    failedStudents = []

    for i in students:
        average = 0
        for x in students["subjects"].items():
            average = average + x
        average = average / len(students[i]["subjects"])

        if average >= 70:
            approvedStudents.append(i)
        else:
            failedStudents.append(i)


    print("\nThis is the list of approved / passed students: \n")

    for i in approvedStudents:
        print(i)

    print("\nThis is the list of failed students: \n")

    for i in failedStudents:
        print(i)
    