import sqlite3
from Student import Student

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

run = True
while(run):
    print("1. Display All Students and all their attributes")
    print("2. Create Students")
    print("3. Update Students")
    print("4. Delete Students by StudentId")
    print("5. Search/Display students by Major, GPA and Advisor")
    choice = int(input("Select an option. "))

    if choice == 1:
        c.execute("SELECT * FROM StudentDB WHERE isDeleted = 0")
        rows = c.fetchall()
        print(rows)
        for row in rows:
            s = Student(row[0],row[1],row[2],row[3],row[4],row[5])
            print(s.getStudent())
    elif choice == 2:
        id = int(input("ID: "));
        firstName = input("First Name")
        lastName = input("Last Name")
        gpa = float(input("GPA: "))
        major = input("Major:")
        facultyAdvisor = input("Faculty Advisor: ")
        c.execute("INSERT INTO StudentDB('StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted')"
                  "VALUES (?,?,?,?,?,?,?)", (id, firstName, lastName, gpa, major, facultyAdvisor, False))
        conn.commit()
        studentID = c.lastrowid
        print("Record created ", studentID)
    elif choice == 3:
        id = int(input("ID:"))
        c.execute("SELECT StudentID FROM StudentDB WHERE StudentID = {}".format(id))
        row = c.fetchall()
        if row:
            print("Please input major and advisor. Leave blank to avoid changes")
            newM = input("Major: ")
            newA = input("Advisor: ")
            if newM != "":
                c.execute("UPDATE StudentDB SET Major = '{}' WHERE StudentID = {}".format(newM, id))
            if newA != "":
                c.execute("UPDATE StudentDB SET FacultyAdvisor = '{}' WHERE StudentID ={}".format(newA, id))
    elif choice == 4:
        id = int(input("ID:"))
        c.execute("SELECT StudentID FROM StudentDB WHERE StudentID = {}".format(id))
        row = c.fetchall
        if row:
            c.execute("UPDATE StudentDB SET isDeleted = TRUE WHERE StudentID = {}".format(id))
            conn.commit()
        else:
            print("Student not in database. ")
    elif choice == 5:
        search = int(input("Search by \n1. Major \n2.Faculty Advisor \n3.GPA"))
        if search == 1:
            enter = input("Major: ")
            c.execute("SELECT * FROM StudentDB WHERE Major = '{}'".format(enter))
            rows = c.fetchall()
            for row in rows:
                 s = Student(row[0],row[1],row[2],row[3],row[4],row[5])
                 print(s.getStudent())
        elif search == 2:
            enter = input("Faculty Advisor ")
            c.execute("SELECT * FROM StudentDB WHERE FacultyAdvisor = '{}'".format(enter))
            rows = c.fetchall()
            for row in rows:
                s = Student(row[0],row[1],row[2],row[3],row[4],row[5])
                print(s.getStudent())
        elif search == 3:
            enter = float(input("GPA: "))
            c.execute("SELECT * FROM StudentDB WHERE GPA = '{}' ".format(enter))
            rows = c.fetchall()
            for row in rows:
                s = Student(row[0],row[1],row[2],row[3],row[4],row[5])
                print(s.getStudent())
    elif choice == 6:
        run = False