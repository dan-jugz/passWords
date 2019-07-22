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