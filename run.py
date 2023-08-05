import termcolor
import pyfiglet
import random
import re

# Application Title with ASCII art and blue color
app_title = pyfiglet.figlet_format("Passwords Generator", width = 100)
print(termcolor.colored(app_title, color= "blue"))


print(termcolor.colored("Welcome To Your Passwords Generator Application!\n", color = "green"))

def get_user_name():
    """ 
    Simple Function To Get the User Full Name, 
    Then Check On The User Name if it Follows the General Name Syntax "letters" only using (Regular Expression)    
    Say Hi To User though Simple nice Message
    """
    while True:
        fname = input("Please Enter Your First Name: ").strip().capitalize()
        lname = input("Please Enter Your Last Name: ").strip().capitalize()

        if re.search("^[A-z]+$", fname and lname):
            print(f"Hi {fname} {lname}, Nice To See You!")
            break

        else:
            try:
                raise ValueError(
                    f"Please Write A Correct Name!"
                )
            except ValueError as e:
                print(f"Invalid Name: {e}, please try again. \n")

get_user_name()