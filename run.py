#!/usr/bin/env python3.6
from user import User
from cred import Info


def create_account(name,e_mail):
    '''
    creating a new account
    '''
    new_user=User(name,e_mail)
    return new_user

def create_credentials(facebk_pass,email_pass):
    '''
    create credentials of password and email
    '''
    new_cred=Info(facebk_pass,email_pass)
    return new_cred

def save_account(user):
    '''
    save the user 
    '''
    user.save_user()

def save_credentials(cred):
    '''
    a method to save new user account
    '''
    cred.save_info()

def display_users():
    '''
    a method to display the users already using this password locker
    '''
    return User.display_users()

def user_log_in(name, password):
    '''
    function that allows a user to log in to their account to view or change details
    '''
    verified_user= User.user_verified(name,password)
    return verified_user

def display_creds():
    '''
    method that displays the various credentials that you have logged into the app
    '''
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
4. gs - GENERATE PASSWORDS
5. lg - LOGIN TO YOUR ACCOUNT""")

        print(" ")
        print("      TYPE IN A SHORT CODE!")
        print(" ")

        short_code = input() .lower()
        if short_code =='cc':
            print(" ")
            print("-" * 130)
            print("    ***CREATE A NEW ACCOUNT!")
            print(" ")
            print("what is your first name?..")
            print(" ")
            name= input()
            print("what is your new account name?..")
            print(" ")
            acct= input()
            print("what is your account password?")
            print(" ")
            acct_pass=input()
            save_account(create_account(name,acct))
            print('\n')
            save_credentials(create_credentials (acct,acct_pass))
            print('\n')
            print("-" * 100)
            print(f"New Account { name} { acct } has been created")
            print('\n')
        elif short_code =='dac':
            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{acct}")
                for cred in display_creds():
                    print (f"{acct_pass}")
                    print(" ")
            else:
                    print('\n')
                    print("-" * 130)
                    print(" ")
                    print("                 ***  PLEASE CREATE AN ACCOUNT ")
                    print("                   *** You have not created an account yet :( ")
                    print(" ")

        elif short_code == "lg":
            '''
            Logs in user to the password locker account
            '''
            print('\n')
            print("*"*32)    
            print("Log into Password Locker Account")
            print("*"*32)

            print("Enter User Name")
            user_name = input()
            
            print("Enter Password")
            user_password = input()


            if  user_log_in(user_name,user_password):
                print('\n')
                print("-"*130)    
                print(f"Welcome {user_name} to your Credentials" )
                print("-"*130)

                while True:
                    '''
                    Loop to run functionalities after successful login
                    '''
                    print('''Use these short code to navigate \n
                        cc:Create a new credential \n
                        dc:Display saved credentials \n
                        gc:Generate credential with a random password\n
                        dl:Delete credential\n    
                        ex:Log out of credential account           ''')

                    #get short code from user
                    short_code = input().lower()

                    if short_code == "cc":
                        '''
                        Creating a credential
                        '''
                        print('\n')
                        print("New Credential")
                        print("-"*15)

                        print("Name of the Credential...")   
                        credential_name = input()

                        print("Password of the Credential...")
                        credential_password = input()

                        #create and save credential
                        save_credentials( create_credentials(credential_name,credential_password)
                        )

                        print('\n')
                        print(f"Credentials for *{credential_name}* has been created and saved successfully")
                        print('\n')
        elif short_code =='gs':
            print(" ")
            print("   ***TO GENERATE A PASSWORD, ENTER YOUR NAME AND ACCOUNT BELOW! ")
            print(" ")
            list_of_inputs = [c for c in input()]
            list_of_inputs.reverse()
            print(list_of_inputs)

        elif short_code == "ex":
            print("-"*130)
            print(" ")
            print("                        THAX FOR DROPING IN!")
            print("                           Bye Bye..xoxo.")
            print(" ")
            print("-" * 130)
            break
        else:
            print("-" * 130)
            print("                             ++ RETRY!!")
            print(" ")
            print("                Please Select One Of The Options Provided")
            print(" ")

if __name__ == '__main__':

    main()
