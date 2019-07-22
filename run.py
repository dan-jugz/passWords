#!/usr/bin/env python3.6
from user import User
from cred import Info


def create_account(name,e_mail):
    new_user=User(name,e_mail)
    return new_user

def create_credentials(facebk_pass,email_pass):
    new_cred=Info(facebk_pass,email_pass)
    return new_cred

def save_account(user):
    user.save_user()

def save_credentials(cred):
    cred.save_info()

def display_users():
    return User.display_users()

def display_creds():
    return Info.display_info()

def main():
    print(" ")
    print("HELLO THERE  WELCOME!!")
    print(" ")
    print(" ")
    while True:
        print("-" * 130)
        print("""USE THE FOLLOWING SHORT CODES!!
1. cc - CREATE NEW ACCOUNT
2. ex - EXIT PASSWORD LOCK
3. dac - DISPLAY ACCOUNTS
4. gs - GENERATE PASSWORDS""")

        print(" ")
        print("      TYPE IN A SHORT CODE!")
        print(" ")

        short_code = input() .lower()
        if short_code =='cc':
            print(" ")
            print("-" * 156)
            print("    ***CREATE A NEW ACCOUNT!")
            print(" ")
            print("what is your first name?..")
            print(" ")
            name= input()
            print("what is your email address?..")
            print(" ")
            email= input()
            print("what is your facebook password?")
            print(" ")
            facebk_pass=input()