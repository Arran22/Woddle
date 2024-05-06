from abc import ABC, abstractmethod

from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

from interaction.db_interaction import database_manager

from user import *

import re

db = database_manager()

class account_manipulation_base(ABC):

    def sign_up_or_in(self):
    
        validated = False

        while validated == False:
            up_or_in = Prompt.ask("Do you have an account? (Y/N)")

            input_dict = {
                'N': ('Create a new account 🔒', self.sign_up),
                'Y': ('Sign in to an existing account 🔑', self.sign_in)
            }
            # Checks if user has an account, and redirects to sign up or sign in page
            
            result = self.handle_sign_up_in(up_or_in, input_dict)
            if result:
                break
        return result

            # if up_or_in.upper() == "N":
            #     validated == True
            #     sign_up()
            # elif up_or_in.upper() == "Y":
            #     validated == True
            #     sign_in()
            # else:
            #     print("Please enter either Y or N to Sign in/up")

    def sign_up(self):

        valid = False
        
        print("Signing up...")

        while valid == False:
            username = Prompt.ask("Enter your username")
            valid = self.check_username_exists(username)

            if not valid:
                print(Panel("Username does not exist, Youre so original!", style="bold green"))

        valid = False
        while valid == False:
            password = Prompt.ask("Enter your password")
            confirm_password = Prompt.ask("Please Re-enter your Password")
            valid = password == confirm_password and bool(re.search(r'\d', password)) and bool(re.search(r'\w', password))

            if not valid:
                print(Panel("Passwords must match and include letters and numbers, [bold]Please try again", style="red"))

        # Creates new user
        new_user = user(username, password, 0)
        db.insert_user(new_user.username, new_user.password)
        return db.get_user_by_name(username)[0][0]
    
    def sign_in(self):

        username = None
        valid = False
        signed_in = False
        
        print("Signing in...")

        # Loop to check if username exists in the database 
        while not valid:
            username = Prompt.ask("Enter your Username")
                
            valid = self.check_username_exists(username)

            if not valid:
                print(Panel("Username does not exist, Please try again.", style="bold red"))

        # Loop to check if password matches username
        valid = False
        while not valid:
            password = Prompt.ask("Enter your Password", password=True).lower()
            
            valid = self.check_password_matches(password, username)

            if not valid:
                print(Panel("Incorrect password, Please try again.", style="bold red"))
        signed_in = True
        return signed_in, db.get_user_by_name(username)[0][0]
        

    def check_username_exists(self,username):
        users = db.get_users()
        #Loops over all user objects and checks if the username exists
        for user in users:
            if user[1].lower() == username.lower():
                return True

    def check_password_matches(self, password, username):
        #Accesses the user with the username entered
        raw_user = db.get_user_by_name(username)
        user_to_check = user(raw_user[0][1], raw_user[0][2], raw_user[0][0], decode=True)

        return user_to_check.compare_password(password)

    def handle_sign_up_in(self, user_input, input_dict):
        if user_input in input_dict:
                description, func = input_dict[user_input]
                return func()
        else:
            print("Please enter Y to Sign In and N to Sign Up")

    def get_user_id(self, user):
        id = db.get_user_by_name(user.username)[0][0]

class account_manipulation(account_manipulation_base):

    def __init__(self):
        self.user = self.sign_up_or_in()

    def get_response(self):
        return self.user

class account_manipulation_test(account_manipulation_base):

    def __init__(self):
        pass