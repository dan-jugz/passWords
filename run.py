
from user import User
from cred import Info


def create_account(name,mail):
    new_user=User(name,mail)
    return new_user

def create_credentials(facebk_pass,email_pass):
    new_cred=Info(facebk_pass,email_pass)
    return new_cred

    