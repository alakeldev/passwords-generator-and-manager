import termcolor
import pyfiglet
import random
import re
import codecs
import os
from cryptography.fernet import Fernet

MIN_CHARS_IN_NAME_AND_PWD = 1
SYMMETRIC_KEY_FILE = "the-security-key.key"
PWDS_FILE = "my-passwords.txt"
PWDS_ECRYPTED_FILE = "my-encrypted-data.txt"


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
            and len(fname) > MIN_CHARS_IN_NAME_AND_PWD
            and len(lname) > MIN_CHARS_IN_NAME_AND_PWD
        ):
            global hi_msg
            hi_msg = f"\nHi {fname} {lname}, nice to see you"
            print(termcolor.colored(hi_msg + "!.\n", color="green"))
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


def pwd_generator_start():
    """
    While: to ask the user if wants to generate new password
    If: to check the four possible scenarios:(yes,no,exit,other)
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
        elif ask_user == "n" or ask_user == "no":
            exit_pwd_generator()
            return False
        elif ask_user == "exit":
            print(termcolor.colored("\nGoodbye! See You Later", color="green"))
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


def exit_pwd_generator():
    """
    Function for asking the user if wants
    exit passwords generator application or not,
    through while: three possible scenarios:(yes,no,other)
    """
    while True:
        print(
            termcolor.colored(
                "\nDo you want to exit the Passwords Generator Application?",
                color="yellow"
            )
        )
        exit_gen = input("'y/n' or 'yes/no': ").lower().strip()
        if exit_gen == "y" or exit_gen == "yes":
            print(termcolor.colored("\nGoodbye! See You Later", color="green"))
            pwd_manager_start()
            return False
        elif exit_gen == "n" or exit_gen == "n":
            print("\n", end="")
            pwd_generator_start()
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only [yes/no OR y/n]. No other values"
                )
            except ValueError as e:
                print(
                    termcolor.colored(f"\nInvalid Value: {e}.", color="red")
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
                        f"Invalid Value: {e}Please try again.", color="red"
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
            exit_pwd_generator()
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
                    "Welcome To Your Passwords Manager Application!",
                    color="green",
                )
            )
            print(termcolor.colored(hi_msg + " again.\n", color="green"))
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
    If: to check the four possible scenarios:(save,view,exit,other)
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
            msg = "\nPlease don't enter empty Fields or only one Character!"
            print(termcolor.colored(msg, color="yellow"))
            user_name = input("Username: ").strip().replace(" ", "")
            new_password = input("Password: ").strip().replace(" ", "")
            if (
                user_name != ""
                and new_password != ""
                and len(user_name) > MIN_CHARS_IN_NAME_AND_PWD
                and len(new_password) > MIN_CHARS_IN_NAME_AND_PWD
            ):
                password_file = codecs.open(
                    PWDS_FILE, "a", encoding="utf-8"
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
                encrypt_data()
            else:
                print(
                    termcolor.colored(
                        "\nEmpty fields or one Character are NOT accepted.",
                        color="red",
                        )
                )
                print(
                    termcolor.colored(
                        "\nAgain please check your choice below:",
                        color="yellow",
                    )
                )
        elif user == "view":
            password_file = codecs.open(
                PWDS_FILE, "r", encoding="utf-8"
            )
            if os.path.getsize(PWDS_FILE) != 0:
                print("\nThe following are the saved ones: \n")
                encrypt_data()
                decrypt_data()
            else:
                msg = "\nYou don't have previous saved Passwords!\n"
                print(termcolor.colored(msg, color="yellow"))
        elif user == "exit":
            print("\n", end="")
            if os.path.getsize(PWDS_FILE) != 0:
                delete_data_start()
                return False
            else:
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
    sym_new_file = open(SYMMETRIC_KEY_FILE, "wb")
    sym_new_file.write(the_sym_key)
    sym_new_file.close()


def encrypt_data():
    """
    Function to take the data from the file (my-passwords.txt)
    and Encrypt these data with the symmetric key
    then create a new file (my-encrypted-data.txt) and
    store the encryption data inside it
    """
    sym_file = open(SYMMETRIC_KEY_FILE, "rb")
    sym_key = sym_file.read()
    sym_file.close()
    pwds_file = open(PWDS_FILE, "rb")
    pwds_file_data = pwds_file.read()
    pwds_file.close()
    f_key = Fernet(sym_key)
    encrypted_data = f_key.encrypt(pwds_file_data)
    encrypted_file = open(PWDS_ECRYPTED_FILE, "wb")
    encrypted_file.write(encrypted_data)
    encrypted_file.close()


def decrypt_data():
    """
    Function to take the encrypted data from(my-encrypted-data.txt)
    and decrypt these data with same symmetric key
    Then print the normal data on the terminal
    """
    sym_file = open(SYMMETRIC_KEY_FILE, "rb")
    sym_key = sym_file.read()
    sym_file.close()
    encrypted_file = open(PWDS_ECRYPTED_FILE, "rb")
    encrypted_data = encrypted_file.read()
    encrypted_file.close()
    f_key = Fernet(sym_key)
    decrypted_data = f_key.decrypt(encrypted_data)
    print(termcolor.colored(decrypted_data.decode(), color="green"))


def delete_files_content():
    ''' Function to delete the content of my saved PWDs and usernames '''
    my_pwd_file = open(PWDS_FILE, "w")
    my_pwd_file.close()
    if os.path.isfile(PWDS_ECRYPTED_FILE):
        my_encry_file = open(PWDS_ECRYPTED_FILE, "w")
        my_encry_file.close()


def delete_data_start():
    """
    Function to ask the user if wants to delete all
    saved passwords and usernames, and it works with
    three possible scenarios:(yes,no,other)
    """
    while True:
        print(
            termcolor.colored(
                "Would you like to delete all "
                "previously saved data before exiting?",
                color="yellow"
            )
        )
        remove_data = input("'y/n' or 'yes/no': ").lower().strip()
        if remove_data == "y" or remove_data == "yes":
            delete_files_content()
            print(
                termcolor.colored(
                    "\nAll Deleted Successfully!\n",
                    color="green"
                )
            )
            return False
        elif remove_data == "n" or remove_data == "no":
            print("\n", end="")
            return False
        else:
            try:
                raise ValueError(
                    f"Please enter only [yes/no OR y/n]. No other values"
                )
            except ValueError as e:
                print(
                    termcolor.colored(
                        f"\nInvalid Value: {e}. Please try again.\n",
                        color="red",
                    )
                )


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
    pwd_generator_start()
    print("Goodbye! Thank You For Using Our Applications.\n")


main()
