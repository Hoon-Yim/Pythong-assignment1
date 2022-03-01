# Ms. Laily Ajeliu
# Assignment 1
# Seunghun Yim 101325908

from asyncio.windows_events import NULL
from genericpath import exists
import sys
from pyparsing import null_debug_action
from wcwidth import wcswidth
from input_validation import *

employee_list = []
item_list = []

# Asks if the use wants to store more employees or items
def close_or_not(type):
    while True:
        yes_or_no = input(f"Another {type}? [y/n] ")
        if yes_or_no == 'y':
            return False
        elif yes_or_no == 'n':
            while True:
                yes_or_no = input("Go to main menu? [y/n] ")
                if yes_or_no == 'y':
                    return True
                elif yes_or_no == 'n':
                    sys.exit("Exiting Application..")
                else:
                    print("Enter between 'y' or 'n'..")
        else:
            print("Enter between 'y' or 'n'..")

# Checks if the employee id or discount is unique
def is_employee_element_unique(value, index):
    for employee in employee_list:
        if employee[index] == value:
            return False
    return True

# Creating Employee
def create_employee():
    NO_entered = False
    halt_statement = "Creating Employee Halt"

    employee_id, NO_entered = int_input("Please enter an Employee's ID: ")
    if NO_entered:
        print(halt_statement)
        return
    employee_name, NO_entered = str_input(
        "Please enter the name of Employee: ")
    if NO_entered:
        print(halt_statement)
        return
    employee_type, NO_entered = type_input("Please enter the Employee Type: ")
    if NO_entered:
        print(halt_statement)
        return
    worked_years, NO_entered = int_input(
        "Please enter how many years this Employee worked: ")
    if NO_entered:
        print(halt_statement)
        return
    total_purchased = 0
    total_discount = 0
    employee_discount, NO_entered = int_input(
        "Please enter the Employee's discount number: ")
    if NO_entered:
        print(halt_statement)
        return

    # check to make the id and discount unique
    if not is_employee_element_unique(employee_id, 0):
        print(f"Employee ID {employee_id} exists in the list already..")
        return
    if not is_employee_element_unique(employee_discount, 6):
        print(
            f"Employee Discount {employee_discount} exists in the list already..")
        return

    temp_list = [employee_id, employee_name, employee_type,
                 worked_years, total_purchased, total_discount, employee_discount]
    employee_list.append(temp_list)
    print(employee_list)

# Checks if the item id is unique
def is_item_id_unique(id):
    for item in item_list:
        if item[0] == id:
            return False
    return True

# Creating Item
def create_item():
    NO_entered = False
    halt_statement = "Creating Employee Halt"

    item_id, NO_entered = int_input("Please enter an Item's ID: ")
    if NO_entered:
        print(halt_statement)
        return
    item_name, NO_entered = str_input("Please enter the Item's name: ")
    if NO_entered:
        print(halt_statement)
        return
    item_cost, NO_entered = int_input("Please enter the price of the Item: ")
    if NO_entered:
        print(halt_statement)
        return

    # check to make the item id unique
    if not is_item_id_unique(item_id):
        print(f"Item ID {item_id} exists in the list already..")
        return

    temp_list = [item_id, item_name, item_cost]
    item_list.append(temp_list)
    print(item_list)

# Making Purchase
# for formatting
def wcpadding(s, l):
    return s + " " * (l - wcswidth(s))

def print_items():
    if len(item_list) == 0:
        return False
    else:
        print("{0}|{1}|{2}".format(wcpadding("Item Number", 12),
                                   wcpadding("Item Name", 12), wcpadding("Item Cost", 12)))
        for item in item_list:
            print("{0}|{1}|{2}".format(wcpadding(str(item[0]), 12), wcpadding(
                str(item[1]), 12), wcpadding(str(item[2]), 12)))
        return True

# Employee Summary
def print_employees():
    # print employees
    if len(employee_list) == 0:
        print("There is no Employee..")
    else:
        print("{0}|{1}|{2}|{3}|{4}|{5}|{6}".format(wcpadding("Employee ID", 12), wcpadding("Employee Name", 15), wcpadding("Employee Type", 15), wcpadding(
            "Years Worked", 15), wcpadding("Total Purchased", 17), wcpadding("Total Discount", 17), wcpadding("Employee Discount Number", 15)))
        for employee in employee_list:
            print("{0}|{1}|{2}|{3}|{4}|{5}|{6}".format(wcpadding(str(employee[0]), 12), wcpadding(str(employee[1]), 15), wcpadding(str(employee[2]), 15), wcpadding(
                str(employee[3]), 15), wcpadding(str(employee[4]), 17), wcpadding(str(employee[5]), 17), wcpadding(str(employee[6]), 15)))

def calculate_purchase(emp, item):
    if (emp[5] >= 200):
        print(f"Employee {emp[0]} already hit the maximum discount amount\nThere will be no discount..")
        emp[4] += item[2]

    else:
        percent_per_year = emp[3] * 2
        if (percent_per_year > 10):
            percent_per_year = 10
        if (emp[2] == "manager"):
            percent_per_year += 10
        else:
            percent_per_year += 2
        percent_per_year /= 100

        emp[5] += item[2] * percent_per_year
        emp[4] += item[2] - (item[2] * percent_per_year)

    return

def check_employee_and_item():
    employee_exist = False
    emp = NULL
    while not employee_exist:
        discount_num, _ = int_input(
            "Please enter the Employee's discount number: ")
        for employee in employee_list:
            if employee[6] == discount_num:
                emp = employee
                employee_exist = True
                break
        if not employee_exist:
            print(
                f"There is no employee who has {discount_num} as a discount number..")

    item_exist = False
    it = NULL
    while not item_exist:
        item_num, _ = int_input("Please enter an Item's ID: ")
        for item in item_list:
            if item[0] == item_num:
                it = item
                item_exist = True
                break
        if not item_exist:
            print(f"There is no item {item_num} to purchase..")

    calculate_purchase(emp, it)

def make_purchase():
    if not print_items():
        print("Since there is no item, you cannot make a purchase..")
        return
    elif len(employee_list) == 0:
        print("Since there is no employee, you cannot make a purchase")
    else:
        while True:
            check_employee_and_item()
            yes_or_no = input("\nAnother purchase? [y/n] ")
            if yes_or_no == 'n':
                break
            elif yes_or_no == 'y':
                continue
            else:
                print("Enter between 'y' or 'n'..")

        print("\nㅡㅡㅡㅡㅡResultㅡㅡㅡㅡㅡ")
        print_employees()

        while True:
            yes_or_no = input("\nGo to main menu? [y/n] ")
            if yes_or_no == 'y':
                return
            elif yes_or_no == 'n':
                sys.exit("Exiting Application..")
            else:
                print("Enter between 'y' or 'n'..")

# Pages
def create_employee_page():
    print("\nㅡㅡㅡㅡㅡ Employee Creation ㅡㅡㅡㅡㅡ")
    while True:
        create_employee()
        while True:
            if close_or_not("Employee"):
                return
            else:
                break

def create_item_page():
    print("\nㅡㅡㅡㅡㅡ Item Creation ㅡㅡㅡㅡㅡ")
    while True:
        create_item()
        while True:
            if close_or_not("Item"):
                return
            else:
                break

def make_purchase_page():
    print("\nㅡㅡㅡㅡㅡ Making Purchase ㅡㅡㅡㅡㅡ")
    make_purchase()

def print_employees_page():
    print("\nㅡㅡㅡㅡㅡ Employees List ㅡㅡㅡㅡㅡ")
    print_employees()

def print_menu():
    print("\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("| 1-Create Employee      |")
    print("| 2-Create Item          |")
    print("| 3-Make Purchase        |")
    print("| 4-All Employee Summary |")
    print("| 5-Exit                 |")
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n")

def run():
    while True:
        print_menu()
        choice, _ = int_input("Please enter your choice: ")
        if choice == 1:
            create_employee_page()
        elif choice == 2:
            create_item_page()
        elif choice == 3:
            make_purchase_page()
        elif choice == 4:
            print_employees_page()
        elif choice == 5:
            sys.exit("Exiting Application..")

run()