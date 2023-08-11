import termcolor
import pyfiglet
import random
import re
import codecs
import os


def get_user_name():
    """
    While: to get the user first & last name
    If: to check on fname & lname that are following general name syntax
    (letters & more than one letter)
    try: to raise a valueError if user enter other than letters
    """
    while True:
        fname = input("Please Enter Your First Name: ").strip().capitalize()
        lname = input("Please Enter Your Last Name: ").strip().capitalize()
        if re.search("^[A-z]+$", fname) and re.search("^[A-z]+$", lname) and len(fname) > 1 and len(lname) > 1:
            print(termcolor.colored(f"\nHi {fname} {lname}, Nice To See You!. \n", color="green"))
            break
        else:
            try:
                raise ValueError(
                    f"Please Write Real-Correct Name Using Letters Only!"
                )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Name: {e}.\n", color="red"))


def pwd_generator():
    """
    While: to ask the user if wants to generate new password
    If: to check the three possible scenarios:(yes,no,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        ask_user = input("Do You Want to Generate a New Password?\n'y/n' or 'yes/no': ").lower().strip()
        if ask_user == "y" or ask_user == "yes":
            pwd_chars_number()
            break
        elif ask_user == "n" or ask_user == "no":
            pwd_manager_start()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter yes/no or y/n. Sorry! no other values available"
                            )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}.\n", color="red"))


def pwd_chars_number():
    """
    While: to ask the user how many Chars wants in new PWD
    If: to control user input (only numbers and between 3-40)
    Try: to raise a valueError if user enter other than
    (only numbers and between 4-40)
    """
    while True:
        pwd_len = input("How many Chars do you want in your password?\n'Min = 4' & 'Max = 40': ").strip()
        print("\n", end="")
        if re.search("^\d+$", pwd_len) and 3 < int(pwd_len) < 41:
            PWD_CHARACTERS = "qwertzuiopü+asdfghjklöä#yxcvbnm,.-!§$%&/()=?ß#><-*/@\12345678}9[]ß{+ZQ"
            pwd = ""
            new_password = termcolor.colored(pwd.join(random.sample(PWD_CHARACTERS, int(pwd_len))), color="green")
            print(f"Your New Password Is: {new_password} \n")
            pwd_second_generator()
            return False
        else:
            try:
                raise ValueError(
                    f"Please Enter Only Numbers and Only Between(4 to 40).\n"
                    )
            except ValueError as e:
                print(termcolor.colored(f"Invalid Value: {e}Please try again.\n", color="red"))


def pwd_second_generator():
    """
    While: to check with the user if wants another new PWD
    after the first one that generated.
    If: to check the three possible scenarios:(yes,no,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        another_pwd = input("Do you want Another new Password?\n'y/n' or 'yes/no': ").lower().strip()
        if another_pwd == "yes" or another_pwd == "y":
            pwd_chars_number()
            return False
        elif another_pwd == "no" or another_pwd == "n":
            pwd_manager_start()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter yes/no or y/n. Sorry! no other values available"
                    )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}.\n", color="red"))


def pwd_manager_start():
    """
    While: to ask the user if wants to run the second app
    If: to check the three possible scenarios:(yes,no,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        passwords_manager = input("\nDo you want to start the Passwords Manager Application?\n'y/n' or 'yes/no': ").lower().strip()
        if passwords_manager == "y" or passwords_manager == "yes":
            app_second_title = pyfiglet.figlet_format("Passwords Manager", font="small", width=100)
            print(termcolor.colored(app_second_title, color="green"))
            print(termcolor.colored("Welcome To Your Passwords Manager Application!\n", color="green"))
            pwd_manager_run()
            break
        elif passwords_manager == "n" or passwords_manager == "no":
            print(termcolor.colored("\nOk, See You Later!.", color="green"))
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter yes/no or y/n. Sorry! no other values available"
                    )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}.", color="red"))


def pwd_manager_run():
    """
    While: to ask user if wants to save new pwd or only view the old ones
    If: to check the three possible scenarios:(save,view,other)
    If nested inside save scenario: to check the user inputs
    (not empty & more than two Chars)
    If nested inside view scenario: to check if the file is empty
    and show msg to user related to status of the file
    For inside view scenario: to loop on each line inside the file
    and print it on terminal
    Try: to raise a valueError if user enter other than (Save and View)
    """
    while True:
        user = input("Do you want to save a new password or only view the previous ones?\n'save' or 'view': ").lower().strip()
        if user == "save":
            msg = "\nPlease Don't Enter Empty Fields or even 1-2 Chars!"
            print(termcolor.colored(msg, color="green"))
            user_name = input("Username: ").strip()
            new_password = input("Password: ").strip()
            if user_name != "" and new_password != "" and len(user_name) > 2 and len(new_password) > 2:
                password_file = codecs.open("my-passwords.txt", "a", encoding="utf-8")
                password_file.write(f"Username: {user_name} | Password: {new_password}\n")
                password_file.close()
                print(termcolor.colored("\nSaved Successfully!.\n", color="green"))
            else:
                print(termcolor.colored("\Empty fields are NOT accepted as Values.\nAgain please check your choice!\n", color="red"))
                continue
        elif user == "view":
            password_file = codecs.open("my-passwords.txt", "r", encoding="utf-8")
            if os.path.getsize("my-passwords.txt") != 0:
                print("\nThe following are the saved ones: \n")
                for pwd in password_file.readlines():
                    print(termcolor.colored(pwd, color="green"))
                    password_file.close()
                break
            else:
                msg = "\nYou Don't Have previous Saved Passwords!\n"
                print(termcolor.colored(msg, color="red"))
        else:
            try:
                raise ValueError(
                    f"Please enter 'save' or 'view'. Sorry! no other choices"
                    )
            except ValueError as e:
                print(termcolor.colored(f"\nInvalid Value: {e}. Please try again.\n", color="red"))


def main():
    ''' Main Function to run the main App code inside it '''
    app_title = pyfiglet.figlet_format("Passwords Generator", font="small", width=100)
    print(termcolor.colored(app_title, color="green"))
    print(termcolor.colored("Welcome To Your Passwords Generator Application!\n", color="green"))
    get_user_name()
    pwd_generator()
    print("Goodbye! Thank You For Using Our Applications.\n")


main()
