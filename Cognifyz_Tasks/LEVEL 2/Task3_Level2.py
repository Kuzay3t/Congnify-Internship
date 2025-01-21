# This is taks 2 of Level 2
# The excercise is to create a password checker for the user
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = input("Enter a password: \n")

def password_checker(password):
    if len(password) > 8:
        cap_letters = [ cap_letter for cap_letter in password if cap_letter in capital_letters]
        caps = len(cap_letters)
        low_letters = [ low_letter for low_letter in password if low_letter in lowercase_letters]
        lows = len(low_letters)
        special_chars = [ special_char for special_char in password if special_char in special_characters]
        specials = len(special_chars)            
        nums = [ num for num in password if num in numbers] 
        num = len(nums)
        if caps >= 2 and lows >= 2 and specials >= 2 and num >= 2:
            print("The Password is strong")
        else:
            print("The Password is weak")
    elif len(password) < 8:
        print("Password is too short")
        
password_checker(password)