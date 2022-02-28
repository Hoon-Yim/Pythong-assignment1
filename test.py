# Lab Professor: Ms. Laily Ajellu
# Assignment 1 
# Jooyoung Song 101022942

from operator import truediv
import sys

employee_list = []
itme_list = []

def menu():
    while True:
        print("----------------------------------")
        print("|      1. Create Employee        |")
        print("|      2. Create Item            |")
        print("|      3. Make Purchase          |")
        print("|      4. All Employee Summary   |")
        print("|      5. Exit                   |")
        print("----------------------------------")
        option = int(input("Please enter your choice: "))
        if (option == 1):
            createEmployee()
        elif (option == 2):
            createItem()
        elif (option == 3):
            makePurchase()
        elif (option == 4):
            summary()
        else:
            print("Good Bye")
            break

def createEmployee():
    while True:
        employeeNum = int(input("Please enter employee number: "))
        for emp in employee_list:
            while employeeNum == emp[0]:
                print("Employee number exists please enter another number")
                employeeNum = int(input("Please enter employee number: "))
                if employeeNum != emp[0]:
                    continue
        employeeName = str(input("Please enter employee's full name: "))
        empType = int(input("Choose from the following employee type: \n1. Manager \n2. Hourly \n"))
        while empType >= 4:
            if empType == 1:
                str(empType == "Manager")
                return
            elif empType == 2:
                str(empType == "Hourly")
                return
            else:
                empType = int(input("Wrong Input!! \nPlease enter which type of the employee: \n1. Manager \n2. Hourly: \n"))
        years = int(input("Please enter how many years the employee has worked: "))
        totalPurchased = 0
        totalDiscount = 0
        empDiscNum = int(input("Please enter employee's discount number: "))

        employees = [employeeNum, employeeName, empType, years, totalPurchased, totalDiscount, empDiscNum]
        employee_list.append(employees)
        print(employee_list)
        if yesNo("employee") == False:
            return

def createItem():
    print("item")

def makePurchase():
    print("purchase")

def summary():
    print("summary")

def yesNo(option):
    while True:
        yesno = input(f"Would you like to add another {option}?")
        if (yesno == "y" or yesno == "Y"):
            return True
        elif (yesno == "n" or yesno == "N"):
            while True:
                menu = input("Would you like to go back to main menu?")
                if (menu == "y" or menu == "Y"):
                        return False
                elif (menu == "n" or menu == "N"):
                    sys.exit("Good bye")
                else:
                    print("Wrong input, please enter either y or n")
        else:
            print("Wrong input, please enter either y or n")

menu()