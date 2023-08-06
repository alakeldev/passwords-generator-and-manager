import termcolor
import pyfiglet
import random
import re

# Application Title with ASCII art and blue color
app_title = pyfiglet.figlet_format("Passwords Generator", width = 100)
print(termcolor.colored(app_title, color= "blue"))


print(termcolor.colored("Welcome To Your Passwords Generator Application!\n", color = "blue"))

def get_user_name():
    """ 
    Simple Function To Get the User Full Name, 
    Then Check On The User Name if it Follows the General Name Syntax "letters" only => using (Regular Expression)    
    Say Hi To User through Simple nice Message
    """
    while True:
        fname = input("Please Enter Your First Name: ").strip().capitalize()
        lname = input("Please Enter Your Last Name: ").strip().capitalize()

        if re.search("^[A-z]+$", fname) and re.search("^[A-z]+$", lname):
            print(termcolor.colored(f"\nHi {fname} {lname}, Nice To See You!. \n", color = "blue"))
            break

        else:
            try:
                raise ValueError(
                    f"Please Write a Correct and Real Name Using Letters Only!"
                )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Name: {e}. Please try again.\n", color = "blue"))

get_user_name()


def pwd_generate():
    """ 
    Function that prompts the user to enter the desired length of a new password 
    Then it will Generate the new password from the static variable that we provided
    """
    while True:
        pwd_len = input("How many characters do you want your password to have: ").strip()
        print("\n", end = "")

        if re.search("^\d+$", pwd_len):
            PWD_CHARACTERS = "qwertzuiopü+asdfghjklöä#yxcvbnm,.-!§$%&/()=?ß#><-*/\@12345678}9[]ß{"
            pwd = ""
            new_password = termcolor.colored(pwd.join(random.sample(PWD_CHARACTERS, int(pwd_len))), color="blue")
            print(f"Your New Password Is: {new_password} \n")
            break
        
        else:
            try:
                raise ValueError(
                    f"Write Only Numbers!"
                    )
            except ValueError as p:

                print(termcolor.colored(f"\nInvalid Value: {p}. Please try again.\n", color = "blue"))
        

pwd_generate()