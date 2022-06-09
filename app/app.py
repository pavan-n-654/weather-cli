import os
import sys
from user import User
from db import DB
import dotenv
import re

#([a-zA-z]+)|(((\d+\.\d+)|(\d+)) ((\d+\.\d+)|(\d+)))

dotenv.load_dotenv(".env")

def print_intro():
    print(" __      __                  __   .__                        _________  .__   .__  ",
          "/  \\    /  \\  ____  _____  _/  |_ |  |__    ____ _______     \\_   ___ \\ |  |  |__| ",
          "\\   \\/\\/   /_/ __ \\ \\__  \\ \\   __\\|  |  \\ _/ __ \\_  __ \\    /    \\  \\/ |  |  |  | ",
          " \\        / \\  ___/  / __ \\_|  |  |   Y  \\  ___/ |  | \\/    \\     \\____|  |__|  | ",
          "  \\__/\\  /   \\___  >(____  /|__|  |___|  / \\___  >|__|        \\______  /|____/|__| ",
          "       \\/        \\/      \\/            \\/      \\/                    \\/            ", sep="\n")
    print("\t==========================")

def print_menu(adminMenu):
    print("\tMain Menu")
    print("\t==========")
    print("\t1. Print This Menu")
    print("\t2. Weather Data")
    if adminMenu:
        print("\t3. View All users")
        print("\t4. Add user")
        print("\t5. Delete user")
        print("\t6. Change user password")
        print("\t7. Logout")
    else:
        print("\t 3. Change password")
        print("\t 4. Logout")

def run_choice(user):
    choice = input("\n\tEnter your choice: ")
    print()
    if choice == "1":
        print_menu(user.isAdmin)
    elif choice == "2":
        pass
    else:
        if user.isAdmin:
            if choice == "3":
                user.showUsers()
            elif choice == "4":
                uName = input("\tEnter username: ")
                uPass = input("\tEnter password: ")
                res = user.addUser(uName, uPass)
                if res:
                    print("\tUser added successfully")
                else:
                    print("\tFailed to add user")
            elif choice == "5":
                uName = input("\tEnter username: ")
                res = user.deleteUser(uName)
                if res:
                    print("\tUser deleted successfully")
                else:
                    print("\tFailed to delete user")
            elif choice == "6":
                res = user.changePassword()
                if res:
                    print("\tPassword changed successfully")
                else:
                    print("\tFailed to change password")
            elif choice == "7":
                exit(0)
            else:
                print("\tInvalid choice\n")
                print_menu(user.isAdmin)
        else:
            if choice == "3":
                res = user.changePassword()
                if res:
                    print("\tPassword changed successfully")
                else:
                    print("\tFailed to change password")
            elif choice == "4":
                exit(0)
            else:
                print("\tInvalid choice")
                print_menu(user.isAdmin)

def runtime():
    print_intro()
    uName = input("\tEnter your username: ")
    uPass = input("\tEnter your password: ")
    if uName == "":
        print("\tUsername cannot be empty")
        return runtime()
    user = User(uName)
    if user.login(uPass):
        print("\tLogin successful\n")
        print_menu(user.isAdmin)
        while True:
            run_choice(user)
    else:
        print("\tLogin failed\n")
        return runtime()

if __name__ == "__main__":
    runtime()
