"""Login and Signup website"""
# import required module haslib.
import hashlib
import os

def signup():
    """Function for handling new users"""
    email = input("Enter a new username: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Re-enter your password: ")
    if pwd == conf_pwd:
        enc = pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        print("password matches")
    else:
        print("passowrd does not match. Please try again. \n")

def login():
    """Function for handling existing users"""
    email = input("enter email: ")
    pwd = input("enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    if email == stored_email and auth_hash == stored_pwd:
        print("Login Successful, welcome back.")
    else:
        print("Login failed! \n")

def clear_console():
    """cleas the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

while 1:
    clear_console()
    print("********** Login System **********")
    print("1. Sign-up")
    print("2. Log-in")
    print("3. Exit")
    choice = input("Please make a selection: ")
    if choice == "1":
        clear_console()
        signup()
    elif choice == "2":
        clear_console()
        login()
    elif choice == "3":
        clear_console()
        break
    else:
        clear_console()
        print("Invalid input. Try again.")