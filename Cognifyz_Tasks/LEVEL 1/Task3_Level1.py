# Task 3, Level 1
# Email Validator

email_adress = input("Give me your email adress: ")

def email_checker(email_adress):
    '''The function checks if @ and .com is in the given string
    and validates as an email adress or not'''
    if "@" and ".com" in email_adress:
        print("This is a valid email adress")
    else:
        print("This is not a valid email adress")


email_checker(email_adress)