#import require module hashlib
import hashlib

def signup():
# User sign up function
    email = input("Enter your email address: ")
    pwd = input("Enter your password: ")
    confpwd = input("Re-enter your password: ")
    if pwd == confpwd:
        enc = pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        print("Password matches")
    else:
        print("Password does not match\n")

def login():
#User login function
    email = input("Enter Email ")
    pwd = ("Enter password ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
