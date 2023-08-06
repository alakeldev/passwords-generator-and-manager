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




def pwd_generate():
    """ 
    Function to ask the user if he wants to generate a new password?
    - if "yes": it prompts the user to enter the desired length of a new password 
    Then It's going to check if the user value is a number between 4 and 70 to accept
    and Generate the new password from the static variable that we provided
    - If "No":
    - If "Other Values" it will start again and push the user to put the expected values to proceed.
    """
    while True:
        ask_user = input("Do You Want to Generate a New Password? 'y/n' or 'yes/no': ").lower().strip()
        print("\n", end = "")

        if ask_user == "y" or ask_user == "yes":
            while True:
                pwd_len = input("How many characters do you want your password to have? 'MIN = 4' & 'MAX = 70': ").strip()
                print("\n", end = "")

                if re.search("^\d+$", pwd_len) and 3 < int(pwd_len) <= 70:
                    PWD_CHARACTERS = "qwertzuiopü+asdfghjklöä#yxcvbnm,.-!§$%&/()=?ß#><-*/\@12345678}9[]ß{+ZQ"
                    pwd = ""
                    new_password = termcolor.colored(pwd.join(random.sample(PWD_CHARACTERS, int(pwd_len))), color="blue")
                    print(f"Your New Password Is: {new_password} \n")
                    break
                
                else:
                    try:
                        raise ValueError(
                            f"Enter a number between 4 and 70. This is the maximum range of characters that can be generated"
                            )
                    except ValueError as p:

                        print(termcolor.colored(f"\nInvalid Value: {p}. Please try again.\n", color = "blue"))
            break

        elif ask_user == "n" or ask_user == "no":
            break

        else:
            try:
                raise ValueError(
                    f"Please enter yes/y or no/n. No other values available"
                            )
            except ValueError as w:

                print(termcolor.colored(f"\nInvalid Value: {w}.\n", color = "blue"))



def main():
    ''' Function to Run All App Functions inside it '''
    get_user_name()
    pwd_generate()

main()
