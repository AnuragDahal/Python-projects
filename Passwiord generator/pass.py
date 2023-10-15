import random
import string

def password():

    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    passlength = int(input("Enter the length of password: "))
    platform=input("Enter the name of platform: ")
    
    # creating an empty list
    key = []

    # adding all the elements to the list using extend() function

    key.extend(list(small_letters))
    key.extend(list(capital_letters))
    key.extend(list(numbers))
    key.extend(list(symbols))
    random.shuffle(key)
    security_key = ("".join(key[:passlength]))

    
    file_input=f"Platform is {platform} and the password is {security_key}\n"
    print(security_key)
    # storing the pass in .txt file      
    with open("my_pass.txt", "a") as f:
        f.writelines(file_input)
    print("Your password has been saved ")
    
    
password()

