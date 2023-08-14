import termcolor
import pyfiglet
import random
import re
import codecs
import os
from cryptography.fernet import Fernet


def get_user_name():
    """
    While: to get the user first & last name
    If: to check on fname & lname that are following general name syntax
    (letters & more than one letter)
    try: to raise a valueError if user enter other than letters
    """
    while True:
        fname = input("Please enter your First Name: ").strip().capitalize()
        lname = input("Please enter your Last Name: ").strip().capitalize()
        if (
            re.search("^[A-z]+$", fname)
            and re.search("^[A-z]+$", lname)
            and len(fname) > 1
            and len(lname) > 1
        ):
            print(
                termcolor.colored(
                    f"\nHi {fname} {lname}, nice to see you!. \n",
                    color="green",
                )
            )
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter real-correct Name using letters only!"
                )
            except ValueError as e:
                print(
                    termcolor.colored(f"\nInvalid Name: {e}.\n", color="red")
                )


def pwd_generator():
    """
    While: to ask the user if wants to generate new password
    If: to check the three possible scenarios:(yes,no|exit,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        exit_msg = termcolor.colored("'exit' => to exit the App", color="red")
        ask_user = (
            input(
                "Do you want to generate a new Password?\n"
                f"{exit_msg}\n"
                "'y/n' or 'yes/no': "
            ).lower()
            .strip()
        )
        if ask_user == "y" or ask_user == "yes":
            pwd_chars_number()
            return False
        elif ask_user == "n" or ask_user == "no" or ask_user == "exit":
            pwd_manager_start()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only [yes/no OR y/n]. No other values"
                )
            except ValueError as e:
                print(
                    termcolor.colored(f"\nInvalid Value: {e}.\n", color="red")
                )


def pwd_chars_number():
    """
    While: to ask the user how many Chars wants in new PWD
    If: to control user input (only numbers and between 4-40)
    Try: to raise a valueError if user enter other than
    numbers and only between 4-40
    """
    while True:
        print("\nHow many Chars do you want in your new Password?")
        pwd_len = input("'Min = 4' & 'Max = 40': ").strip()
        print("\n", end="")
        if re.search("^\d+$", pwd_len) and 3 < int(pwd_len) < 41:
            PWD_CHARACTERS = (
                "qwertzuiopü+asdfghjklöä#yxcvbnm,.-"
                "!§$%&/()=?ß#><-*/@\12345678}9[]ß{+ZQ"
            )
            pwd = ""
            new_password = termcolor.colored(
                pwd.join(random.sample(PWD_CHARACTERS, int(pwd_len))),
                color="green",
            )
            print(f"Your New Password Is: {new_password} \n")
            pwd_second_generator()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only Numbers and only Between(4 to 40).\n"
                )
            except ValueError as e:
                print(
                    termcolor.colored(
                        f"Invalid Value: {e}Please try again.\n", color="red"
                    )
                )


def pwd_second_generator():
    """
    While: to check with the user if wants another new PWD
    after the first one that generated.
    If: to check the three possible scenarios:(yes,no,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        another_pwd = (
            input("Do you want another new Password?\n'y/n' or 'yes/no': ")
            .lower()
            .strip()
        )
        if another_pwd == "yes" or another_pwd == "y":
            pwd_chars_number()
            return False
        elif another_pwd == "no" or another_pwd == "n":
            pwd_manager_start()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only [yes/no OR y/n]. No other values"
                )
            except ValueError as e:
                print(
                    termcolor.colored(f"\nInvalid Value: {e}.\n", color="red")
                )


def pwd_manager_start():
    """
    While: to ask the user if wants to run the second app
    If: to check the three possible scenarios:(yes,no,other)
    Try: to raise a valueError if user enter other values or empty
    """
    while True:
        print("\nDo you want to start the Passwords Manager Application?")
        passwords_manager = input("'y/n' or 'yes/no': ").lower().strip()
        if passwords_manager == "y" or passwords_manager == "yes":
            sym_key()
            app_second_title = pyfiglet.figlet_format(
                "Passwords Manager", font="small", width=100
                )
            print(termcolor.colored(app_second_title, color="green"))
            print(
                termcolor.colored(
                    "Welcome To Your Passwords Manager Application!\n",
                    color="green",
                )
            )
            pwd_manager_run()
            return False
        elif passwords_manager == "n" or passwords_manager == "no":
            print(termcolor.colored("\nOK, See You Later!.\n", color="green"))
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only [yes/no OR y/n]. No other values"
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
    Add exit option to the function
    """
    while True:
        q_msg = (
            "Do you want to save new Password &"
            " its Username or only view previous ones?"
        )
        exit_msg = "'exit' => to exit the App"
        print(q_msg)
        print(termcolor.colored(exit_msg, color="red"))
        user = input("'save' or 'view': ").lower().strip()
        if user == "save":
            msg = "\nPlease don't enter empty Fields or Even 1-2 Chars!"
            print(termcolor.colored(msg, color="green"))
            user_name = input("Username: ").strip()
            new_password = input("Password: ").strip()
            if (
                user_name != ""
                and new_password != ""
                and len(user_name) > 2
                and len(new_password) > 2
            ):
                password_file = codecs.open(
                    "my-passwords.txt", "a", encoding="utf-8"
                )
                password_file.write(
                    f"Username: {user_name} | Password: {new_password}\n"
                )
                password_file.close()
                print(
                    termcolor.colored(
                        "\nSaved Successfully!.\n", color="green"
                    )
                )
            else:
                print(
                    termcolor.colored(
                        "\nEmpty fields or even 1-2 Chars are NOT accepted.",
                        color="red",
                        )
                )
                print(
                    termcolor.colored(
                        "\nAgain check your choice between Save and View.",
                        color="red",
                    )
                )
        elif user == "view":
            password_file = codecs.open(
                "my-passwords.txt", "r", encoding="utf-8"
            )
            if os.path.getsize("my-passwords.txt") != 0:
                print("\nThe following are the saved ones: \n")
                for pwd in password_file.readlines():
                    print(termcolor.colored(pwd, color="green"))
                    password_file.close()
            else:
                msg = "\nYou don't have previous saved Passwords!\n"
                print(termcolor.colored(msg, color="red"))
        elif user == "exit":
            print("\n", end="")
            return False
        else:
            try:
                raise ValueError(f"Please enter only 'save' or 'view'.")
            except ValueError as e:
                print(
                    termcolor.colored(
                        f"\nInvalid Value: {e}. Please try again.\n",
                        color="red",
                    )
                )


def sym_key():
    """
    Function to generate the symmetric key (Security-key)
    Save this key inside new file(the-security-key.key)
    """
    the_sym_key = Fernet.generate_key()
    sym_new_file = open("the-security-key.key", "wb")
    sym_new_file.write(the_sym_key)
    sym_new_file.close()


def main():
    ''' Main Function to run the main App code inside it '''
    app_title = pyfiglet.figlet_format(
        "Passwords Generator", font="small", width=100
    )
    print(termcolor.colored(app_title, color="green"))
    print(
        termcolor.colored(
            "Welcome To Your Passwords Generator Application!\n", color="green"
        )
    )
    get_user_name()
    pwd_generator()
    print("Goodbye! Thank You For Using Our Applications.\n")


main()
