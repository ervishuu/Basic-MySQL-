import mysql.connector

def getConnection():

    try:
        conn = mysql.connector.connect(
            user = 'root',
            password = 'Password123@',
            database = "student_management",
            host='localhost'
        )

    except:
        print("Unable to connection")

    return conn

def insert_data(m,n,o,p,r):
    sql = "INSERT INTO student(Name,Roll_No,Class,Department,Fee_Pending) VALUES(%s,%s,%s,%s,%s)"
    conn = getConnection()
    mm = (m,n,o,p,r)
    myc = conn.cursor()
    try:
        myc.execute(sql,mm)
        conn.commit()
        print("Student ID {} add successfully",myc.lastrowid)

    except:

        conn.rollback()
        print("Erro")

    finally:
        myc.close()
        conn.close()


def DisplY_all_record():

    sql = "SELECT * FROM student"
    conn = getConnection()
    myc = conn.cursor()
    try:
        myc.execute(sql)
        row = myc.fetchone()
        print("{:<20} {:<20} {:20} {:<20} {:<20} {:<20}".format('Student ID', 'Name', 'roll','Class','Department','Fee_Pending'))
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")

        while row is not None:
            StudentID = row[0]
            name = row[1]
            roll = row[2]
            clas = row[3]
            dept = row[4]
            fees = row[5]
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(StudentID, name, roll, clas, dept, fees))
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            row = myc.fetchone()
    except:

        conn.rollback()
        print("Erro")

    finally:
        myc.close()
        conn.close()

def Display_one(n):

    sql = "SELECT * FROM student WHERE stu_ID = %s"
    conn = getConnection()
    myc = conn.cursor()
    mm = (n,)
    try:
        myc.execute(sql,mm)
        row = myc.fetchone()
        if row is None:
            print("Data is not Found...Please Enter valid data")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
            print("{:<20} {:<20} {:20} {:<20} {:<20} {:<20}".format('Student ID', 'Name', 'roll','Class','Department','Fee_Pending'))
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            while row is not None:
                StudentID = row[0]
                name = row[1]
                roll = row[2]
                clas = row[3]
                dept = row[4]
                fees = row[5]

                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(StudentID, name, roll, clas, dept, fees))
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")


                row = myc.fetchone()
    except:

        conn.rollback()
        print("Erro")

    finally:
        myc.close()
        conn.close()

def Update_Data(num3):
    conn = getConnection()
    sql = "SELECT * FROM student WHERE stu_ID = %s"
    myc = conn.cursor()
    mm = (num3,)
    try:
        myc.execute(sql, mm)
        row = myc.fetchone()
        if row is None:
            print("Data is not Found...Please Enter valid data")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
             sql2 = "UPDATE student SET Name=%s,Roll_No=%s ,Class=%s ,Department=%s ,Fee_pending=%s WHERE stu_ID = %s"
             a = input("Enter the Name: ")
             b = int(input("Enter the roll number: "))
             c = input("Enter the class: ")
             d = input("Enter the department: ")
             e = float(input("Enter the pending fees: "))
             data = (a, b, c, d, e, num3)
             myc.execute(sql2 ,data)
             conn.commit()
             print("Data Update sucessfully")
             Display_one(num3)

    except:
        conn.rollback()
        print("Erro")

    finally:
        myc.close()
        conn.close()

def Delete_data():

    delete = int(input("Enter the Student ID Which we want to delete: "))
    conn=getConnection()
    sql = "SELECT * FROM student WHERE stu_ID = %s"
    myc = conn.cursor()
    mm = (delete,)
    try:
        myc.execute(sql, mm)
        row = myc.fetchone()
        if row is None:
            print("Data is not Found...Please Enter valid data")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            sql2 = "DELETE FROM student WHERE stu_ID = %s"
            data = (delete,)
            myc.execute(sql2,data)
            conn.commit()
            print("Record {} Successfully Deleted".format(delete))
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    except:
        conn.rollback()
        print("Erro")

    finally:
        myc.close()
        conn.close()


print("----------------------------------------------------------------------------------------------------------------------------------------------------")

print("Press 1 for Insert Data :")
print("Press 2 Show Record: ")
print("Press 3 Update record: ")
print("Press 4 Delete record: ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")

choice = True

while choice:
    try:

        input1 = int(input("Enter your choice: "))

        if input1 == 1:
            num1 = int(input("Enter how many record you want to Insert: "))
            for i in range(num1):
                a = input("Enter the of student: ")
                b = int(input("Enter the roll number: "))
                c = input("Enter the class: ")
                d = input("Enter the deparment: ")
                e = float(input("Enter the pending fee: "))
                insert_data(a,b,c,d,e)
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            choice = input("Do want to exit(y/n):")
            if choice == "y":
                break

        elif input1 == 2:
            num2 = input("Do you want to display all recored (y/n): ")
            if num2 == "y":
                DisplY_all_record()
                choice = input("Do want to exit(y/n):")
                if choice == "y":
                    break

            else:
                num3 = int(input("Enter the Student ID Which you want to search:"))
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                Display_one(num3)
                choice = input("Do want to exit(y/n):")
                if choice == "y":
                    break

        elif input1 == 3:
            num3 = int(input("Enter the student ID which we want to update: "))
            Update_Data(num3)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            choice = input("Do want to exit(y/n):")
            if choice == "y":
                break

        elif input1 ==4 :
            Delete_data()
            choice = input("Do want to exit(y/n):")
            if choice == "y":
                break

        else:
            input1 = int(input("Enter your choice: "))
    except:
        print(".....Invalid Input..... please try Aaing...")



