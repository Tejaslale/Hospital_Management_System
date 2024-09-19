from os import system
import re
import mysql.connector

# Making Connection
con = mysql.connector.connect(
    host="127.0.0.1", user="root", password="Tejas@12345lale", database="hospital")

# Make a regular expression for validating an Email
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# For validating a Phone Number
phone_pattern = re.compile("(0|91)?[7-9][0-9]{9}")

# Function to Add_Patient
def Add_Patient():
    print("{:>60}".format("-->> Add Patient Record <<--"))
    Id = input("Enter Patient Id: ")
    # Checking If Patient Id Exists or Not
    if (check_patient(Id)):
        print("Patient ID Already Exists\nTry Again..")
        input("Press Any Key To Continue..")
        Add_Patient()
    Name = input("Enter Patient Name: ")
    # Checking If Patient Name Exists or Not
    if (check_patient_name(Name)):
        print("Patient Name Already Exists\nTry Again..")
        input("Press Any Key To Continue..")
        Add_Patient()
    Email_Id = input("Enter Patient Email ID: ")
    if re.fullmatch(email_regex, Email_Id):
        print("Valid Email")
    else:
        print("Invalid Email")
        input("Press Any Key To Continue..")
        Add_Patient()
    Phone_no = input("Enter Patient Phone No.: ")
    if phone_pattern.match(Phone_no):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        input("Press Any Key To Continue..")
        Add_Patient()
    Address = input("Enter Patient Address: ")
    Disease = input("Enter Disease: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Disease)
    # Inserting Patient Details into the Patient (patient_data) Table
    sql = 'INSERT INTO patient_data VALUES (%s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    # Executing the SQL Query
    c.execute(sql, data)
    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Patient Record")
    input("Press Any Key To Continue..")
    menu()

# Function to Check if Patient with given Name Exists or Not
def check_patient_name(patient_name):
    sql = 'SELECT * FROM patient_data WHERE Name=%s'
    c = con.cursor(buffered=True)
    data = (patient_name,)
    c.execute(sql, data)
    r = c.rowcount
    return r == 1

# Function to Check if Patient with given Id Exists or Not
def check_patient(patient_id):
    sql = 'SELECT * FROM patient_data WHERE Id=%s'
    c = con.cursor(buffered=True)
    data = (patient_id,)
    c.execute(sql, data)
    r = c.rowcount
    return r == 1

# Function to Display_Patient
def Display_Patient():
    print("{:>60}".format("-->> Display Patient Record <<--"))
    sql = 'SELECT * FROM patient_data'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Patient Id: ", i[0])
        print("Patient Name: ", i[1])
        print("Patient Email Id: ", i[2])
        print("Patient Phone No.: ", i[3])
        print("Patient Address: ", i[4])
        print("Disease: ", i[5])
        print("\n")
    input("Press Any key To Continue..")
    menu()

# Function to Update_Patient
def Update_Patient():
    print("{:>60}".format("-->> Update Patient Record <<--\n"))
    Id = input("Enter Patient Id: ")
    if not check_patient(Id):
        print("Patient Record Not Exists\nTry Again")
        input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Patient Email ID: ")
        if re.fullmatch(email_regex, Email_Id):
            print("Valid Email")
        else:
            print("Invalid Email")
            input("Press Any Key To Continue..")
            Update_Patient()
        Phone_no = input("Enter Patient Phone No.: ")
        if phone_pattern.match(Phone_no):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            input("Press Any Key To Continue..")
            Update_Patient()
        Address = input("Enter Patient Address: ")
        # Updating Patient details in patient_data Table
        sql = 'UPDATE patient_data SET Email_Id = %s, Phone_no = %s, Address = %s WHERE Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Patient Record")
        input("Press Any Key To Continue..")
        menu()

# Function to Remove_Patient
def Remove_Patient():
    print("{:>60}".format("-->> Remove Patient Record <<--\n"))
    Id = input("Enter Patient Id: ")
    if not check_patient(Id):
        print("Patient Record Not Exists\nTry Again")
        input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'DELETE FROM patient_data WHERE Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Patient Removed")
        input("Press Any Key To Continue..")
        menu()

# Function to Search_Patient
def Search_Patient():
    print("{:>60}".format("-->> Search Patient Record <<--\n"))
    Id = input("Enter Patient Id: ")
    if not check_patient(Id):
        print("Patient Record Not Exists\nTry Again")
        input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'SELECT * FROM patient_data WHERE Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Patient Id: ", i[0])
            print("Patient Name: ", i[1])
            print("Patient Email Id: ", i[2])
            print("Patient Phone No.: ", i[3])
            print("Patient Address: ", i[4])
            print("Disease: ", i[5])
            print("\n")
        input("Press Any key To Continue..")
        menu()

# Menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Hospital Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Patient")
    print("2. Display Patient Record")
    print("3. Update Patient Record")
    print("4. Remove Patient Record")
    print("5. Search Patient Record")
    print("6. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Patient()
    elif ch == 2:
        system("cls")
        Display_Patient()
    elif ch == 3:
        system("cls")
        Update_Patient()
    elif ch == 4:
        system("cls")
        Remove_Patient()
    elif ch == 5:
        system("cls")
        Search_Patient()
    elif ch == 6:
        system("cls")
        print("{:>60}".format("Have A Nice Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        input("Press Any key To Continue..")
        menu()

# Calling menu function
menu()