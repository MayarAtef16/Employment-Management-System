import mysql.connector
from os import system
import re

# making Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jana9jojo",
    database="employee"
)


# mycrusor = con.cursor()
# Function to Display Employee
def Display_Employee():
    print("{:>60}".format("-->> Add Employee Record <<--"))
    # query to select all rows from Employee (empdata) Table
    sql = 'select * from empdata'
    c = con.cursor()

    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employess
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email ID: ", i[2])
        print("Employee Phone Number: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
    menu()


# make a regular expression for validating Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# For validating a Phone Number
pattern = re.compile("(01){1}\d{9}")


# def Phone_Number_validation(Phone_number):
#     my_number = phonenumbers.parse(Phone_number)
#     return phonenumbers.is_valid_number(my_number)


# mycrusor.execute("CREATE DATABASE Employee")
# mycrusor.execute("CREATE TABLE empdata (ID INT(11) PRIMARY KEY,Name VARCHAR(1000),Email_ID TEXT(1000),Phone_no INT("
#                 "11),Address TEXT(1000) ,Post Text(1000),Salary BIGINT(20) )")
# ADD EMPLOY Function
def Add_Employ():
    print("{:<60}".format("-->>Add Employee Record<<--"))
    ID = input("Enter Employee ID: ")
    if check_employee_id(ID):
        print("Employee Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # Checking if Employee Name is Exit or Not
    if check_employee_name(Name):
        print("Employee Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Email_ID = input("Enter Employee Email_ID: ")
    if re.fullmatch(regex, Email_ID):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key to Continue")
        Add_Employ()
    Phone_no = input("Enter Employee Phone_no: ")
    if pattern.match(Phone_no):
        # if Phone_Number_validation(Phone_no):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key to Continue")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (ID, Name, Email_ID, Phone_no, Address, Post, Salary)
    # Inserting Employee Details
    # The Employee (empdata) Table
    sql = "insert into empdata values(%s,%s,%s,%s,%s,%s,%s)"
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()


# Function to Check if Employee with
# give Name Exist or not
def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Name=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Excecute the sql query
    c.execute(sql, data)

    # rowcount method to find with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function to Check if Employee with
# give Name Exist or not
def check_employee_id(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where ID=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Excecute the sql query
    c.execute(sql, data)

    # rowcount method to find with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function to Update Employee
def Update_Employee():
    print("{:>60}".format("-->> Update Emplyee Record <<--"))
    ID = input("Enter Employee ID: ")
    if not check_employee_id(ID):
        print("Employee does not Exist\nTry Again..")
        press = input("Press Any Key To Continue..")
        Update_Employee()
    else:
        # query to select all Rows from
        # employee(empdata) table
        Email_ID = input("Enter Employee Email_ID: ")
        if re.fullmatch(regex, Email_ID):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key to Continue")
            Update_Employee()
        Phone_no = input("Enter Employee Phone_no: ")
        if pattern.match(Phone_no):
            # if Phone_Number_validation(Phone_no):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key to Continue")
            Update_Employee()
        Address = input("Enter Employee Address: ")
        # Updating Employee details in the empdata table
        sql = 'UPDATE empdata set Email_ID=%s,  Phone_no=%s, Address=%s where ID = %s  '
        data = (Email_ID, Phone_no, Address, ID)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to change in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()


# Function To Promote Employee
def Promote_Employee():
    print("{:>60}".format("-->> Promote Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if not check_employee_id(ID):
        print("Employee does not Exist\nTry Again..")
        press = input("Press Any Key To Continue..")
        Promote_Employee()
    else:
        Amount = int(input("Enter Increase Salary: "))
        # query select the sala of the employee
        sql = 'select salary from empdata where ID=%s '
        data = (ID,)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)
        # fetching salary of Emplyee with given ID
        r = c.fetchone()
        t = r[0] + Amount

        # query Update Salary of the Employee
        sql = 'UPDATE empdata set Salary = %s where ID = %s  '
        data2 = (t, ID)

        # Executing the sql query
        c.execute(sql, data2)
        # commit() method to change in the table
        con.commit()
        print("Employee Promoted")
        press = input("Press Any Key To Continue..")
        menu()


# Function To Remove Employee Record
def Remove_Employee():
    print("{:>60}".format("-->> Remove Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if not check_employee_id(ID):
        print("Employee does not Exist\nTry Again..")
        press = input("Press Any Key To Continue..")
        Remove_Employee()
    else:
        # query select the sala of the employee
        sql = 'delete from empdata where ID=%s '
        data = (ID,)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to change in the table
        con.commit()
        print("Employee Record Removed")
        press = input("Press Any Key To Continue..")
        menu()


# Function To Search Employee
def Search_Employee():
    print("{:>60}".format("-->> Search Employee Record <<--"))
    ID = input("Enter Employee ID: ")
    if not check_employee_id(ID):
        print("Employee does not Exist\nTry Again..")
        press = input("Press Any Key To Continue..")
        Search_Employee()
    else:
        # query select the sala of the employee
        sql = 'select * from empdata where ID=%s '
        data = (ID,)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # fetching
        r = c.fetchone()
        print("Employee Id: ", r[0])
        print("Employee Name: ", r[1])
        print("Employee Email ID: ", r[2])
        print("Employee Phone Number: ", r[3])
        print("Employee Address: ", r[4])
        print("Employee Post: ", r[5])
        print("Employee Salary: ", r[6])

        print("Employee Record Searched")
        press = input("Press Any Key To Continue..")
        menu()


# Menu function to display menu

def menu():
    system("cls")
    print("{:<60}".format("**************************"))
    print("{:>60}".format("-->> Employee Management system <<--"))
    print("{:<60}".format("**************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:<60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employee()
    elif ch == 3:
        system("cls")
        Update_Employee()
    elif ch == 4:
        system("cls")
        Promote_Employee()
    elif ch == 5:
        system("cls")
        Remove_Employee()
    elif ch == 6:
        system("cls")
        Search_Employee()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have a Nice Day "))
    else:
        print("Invalid Choice!")
        press = input("Press Any Key To Continue..")
        menu()


# Calling Menu Function
menu()
