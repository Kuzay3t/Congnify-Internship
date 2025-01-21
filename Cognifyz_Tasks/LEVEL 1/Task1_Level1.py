# Task 1 Level !
# A String Rversal function that reverses a given string

string = input("What's the word that you want to reverse? ") # receives user's input that is to be reversed as a string 

def reverse_string(string):
    """ This function reverses the string passed as a parameter """
    n = len(string)
    new_string = ""
    
    for i in range(n): # iterating through the string in reverse order
        new_string += string[n - i - 1]
    print(f'The reversed string is "{new_string}"')

reverse_string(string)
