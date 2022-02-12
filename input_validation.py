def int_input(string):
    while True:
        entered_value = input(string)
        if entered_value == "NO":
            return 0, True
        elif entered_value.isnumeric():
            return int(entered_value), False
        else:
            print("Please enter an interger value..")

def str_input(string):
    while True:
        entered_value = input(string)
        if entered_value:
            if entered_value == "NO":
                return entered_value, True
            else:
                return entered_value, False
        else:
            print("Please enter a value..")

def type_input(string):
    while True:
        entered_value = input(string)
        if entered_value == "NO":
            return entered_value, True
        elif entered_value == "hourly" or entered_value == "manager":
            return entered_value, False
        else:
            print("Please enter the employee type between \"hourly\" and \"manager\"")
