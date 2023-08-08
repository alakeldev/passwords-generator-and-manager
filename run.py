import termcolor
import pyfiglet
import random
import re


def get_user_name():
    """
    Simple Function To Get the User Full Name,
    Then Check On The User Name if it Follows the General Name Syntax "letters"
    through (Regular Expression), also more than two letters.
    Say Hi to user_name through Simple nice Message
    """
    while True:
        fname = input("Please Enter Your First Name: ").strip().capitalize()
        lname = input("Please Enter Your Last Name: ").strip().capitalize()

        if re.search("^[A-z]+$", fname) and re.search("^[A-z]+$", lname) and len(fname) > 2 and len(lname) > 2:
            print(termcolor.colored(f"\nHi {fname} {lname}, Nice To See You!. \n", color="blue"))
            break

        else:
            try:
                raise ValueError(
                    f"Please Write a Correct and Real Name Using Letters Only!"
                )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Name: {e}. Please try again.\n", color="blue"))


def pwd_generator():
    """
    Function to ask the user if he wants to generate a new password? with three scenarios as per below:
    - if "yes": it prompts the user to enter the desired length of a new password
    Then It's going to check if the user value is a number between 4 and 70 to accept it
    and Generate the new password from the static variable that we provided.
    Finally it will ask the user if wants another new password to generate a new one again.
    - If "No": It will skip this part of the app and jump to the part of PWD Manager.
    - If "Other Values" it will show user msg(invalid value) to guide the user.
    Then starts again and push the user to put the expected values to proceed.
    """
    while True:
        ask_user = input("Do You Want to Generate a New Password? 'y/n' or 'yes/no': ").lower().strip()
        if ask_user == "y" or ask_user == "yes":

            while True:
                pwd_len = input("How many characters do you want your password to have? 'MIN = 4' & 'MAX = 70': ").strip()
                print("\n", end="")
                if re.search("^\d+$", pwd_len) and 3 < int(pwd_len) <= 70:
                    PWD_CHARACTERS = "qwertzuiopü+asdfghjklöä#yxcvbnm,.-!§$%&/()=?ß#><-*/@\12345678}9[]ß{+ZQ"
                    pwd = ""
                    new_password = termcolor.colored(pwd.join(random.sample(PWD_CHARACTERS, int(pwd_len))), color="blue")
                    print(f"Your New Password Is: {new_password} \n")

                    while True:
                        another_pwd = input("Do you want Another new Password? 'y/n' or 'yes/no': ").lower().strip()
                        if another_pwd == "yes" or another_pwd == "y":
                            break
                        elif another_pwd == "no" or another_pwd == "n":
                            return False
                        else:
                            try:
                                raise ValueError(
                                    f"Please enter yes/no or y/n. Sorry! no other values available"
                                )
                            except ValueError as e:
                                print(termcolor.colored(f"\nInvalid Value: {e}.\n", color="blue"))
                else:
                    try:
                        raise ValueError(
                            f"Enter a number between 4 and 70. This is the maximum range of characters that can be generated"
                            )
                    except ValueError as e:
                        print(termcolor.colored(f"Invalid Value: {e}. Please try again.\n", color="blue"))

        elif ask_user == "n" or ask_user == "no":
            return False

        else:
            try:
                raise ValueError(
                    f"Please enter yes/no or y/n. Sorry! no other values available"
                            )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}.\n", color="blue"))


def pwd_manager():
    """
    a Function runs:
    while condition that asks the user if wants to start the PWD Manager App
    also a nested while condition to check with the user if wants to save a new password or even
    to check-view the previous ones.
    """
    while True:
        passwords_manager = input("\nDo you want to start the Passwords Manager Application? 'y/n' or 'yes/no': ").lower().strip()
        if passwords_manager == "y" or passwords_manager == "yes":
            app_second_title = pyfiglet.figlet_format("Passwords Manager", font="small", width=100)
            print(termcolor.colored(app_second_title, color="blue"))
            print(termcolor.colored("Welcome To Your Passwords Manager Application!\n", color="blue"))

            while True:
                user = input("Do you want to save a new password or view all your previous saved passwords? 'save' or 'view': ").lower().strip()
                if user == "save":
                    user_name = input("Username: ").strip()
                    new_password = input("Password: ").strip()
                    if user_name != "" and new_password != "" and len(user_name) > 2 and len(new_password) > 2:
                        password_file = open("my-passwords.txt", "a")
                        password_file.write(f"Username: {user_name} |=>| Password: {new_password}\n")
                        password_file.close()
                        print(termcolor.colored("\nAdded Successfully!.\n", color="blue"))
                        continue
                    else:
                        print(termcolor.colored("\nThe empty field or even one-two characters are NOT accepted as a Values. Please again check your choice!\n", color="blue"))
                        continue
                elif user == "view":
                    print("\nThe following are the saved Usernames and Passwords related to your accounts: ")
                    password_file = open("my-passwords.txt", "r")
                    for pwd in password_file.readlines():
                        print(termcolor.colored(pwd, color="blue"), end="")
                    password_file.close()
                    return False
                else:
                    try:
                        raise ValueError(
                            f"Please enter 'save' or 'view'. Sorry! no other choices"
                            )
                    except ValueError as e:
                        print(termcolor.colored(f"\nInvalid Value: {e}. Please try again.\n", color="blue"))

        elif passwords_manager == "n" or passwords_manager == "no":
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter yes/no or y/n. Sorry! no other values available"
                    )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}.", color="blue"))


def main():
    ''' Function to Run All App Functions inside it '''
    get_user_name()
    pwd_generator()
    pwd_manager()
    print(termcolor.colored("\nGoodbye! Thank You For Using Our Applications.", color="blue"))


app_title = pyfiglet.figlet_format("Passwords Generator", font="small", width=100)
print(termcolor.colored(app_title, color="blue"))
print(termcolor.colored("Welcome To Your Passwords Generator Application!\n", color="blue"))
main()
