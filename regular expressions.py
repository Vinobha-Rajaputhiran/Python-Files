#Task: Write a Python program to validate the Regular Expression for the following
#(a) Email Address
#(b) Mobile numbers of Bangladesh
#(c) Telephone numbers of USA
#(d) 16-character alphanumeric password composed of alphabets of UpperCase, LowerCase, Special Characters, and Numbers

input_email= input("Enter your email address: ")
input_BangPH= input("Enter your Bangladesh Phone Number: ")
input_USAPH= input("Enter your USA Phone Number: ")
input_password= input("Enter your password: ")

import re
#Separate functions for each condition are specified in order
def check_email(input_email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    result = re.search(regex, input_email) 
    #True or False value is returned to the result

    if result :
        print("Email address is valid")
    else:
        print("Email address is invalid")

def check_Bangladesh_number(input_BangPH):
        regex = r"/^(?:(?:\+|00)88|01)?\d{11}$/"
        result = re.search(regex, input_BangPH)

        if result:
            print("Bangladesh Phone Number is valid")
        else:
            print("Bangladesh Phone Number is invalid")

def check_USA_phone_number(input_USAPH):
    regex = r"^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$"
    result = re.search(regex, input_USAPH)

    if result:
        print("USA Phone Number is valid")
    else:
        print("USA Phone Number is invalid")

def check_password(input_password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,16}$"
    result = re.search(regex, input_password)

    if result:
        print("Password is valid")
    else:
        print("Password is invalid")

#Call respective functions
check_email(input_email)
check_Bangladesh_number(input_BangPH)
check_USA_phone_number(input_USAPH)
check_password(input_password)






