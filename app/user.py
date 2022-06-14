import os
import sys
app_dir = os.path.dirname(__file__)
sys.path.append(app_dir)
from db import DB
import hashlib

class User:
    def __init__(self, username):
        self.username = username
        self.isAdmin = False
        self.db = DB()
        self.loginstatus = False

    def hash_password(self, string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    def login(self, password):
        if self.loginstatus:
            print('You are already logged in')
            return False
        userdata = self.db.findUser(self.username)
        if userdata and self.hash_password(password) == userdata['password']:
            self.loginstatus = True
            if userdata['role'] == 'admin':
                self.isAdmin = True
            return True
        else:
            return False

    def addUser(self, username, password):
        if not self.isAdmin:
            raise Exception('You are not an admin')

        if username == '':
            print('Username cannot be empty')
            return False
        if password == '':
            print('Password cannot be empty')
            return False

        if self.db.findUser(username):
            return False
        else:
            self.db.insertUser(username, self.hash_password(password))
            return True

    def deleteUser(self, username):
        if not self.isAdmin:
            raise Exception('You are not an admin')

        if self.db.findUser(username):
            self.db.deleteUser(username)
            return True
        else:
            return False

    def changePassword(self):
        username = self.username
        if self.isAdmin:
            username = input('Enter username for password change: ')
        newpassword = input('Enter new password: ')
        if newpassword == '':
            print('Password cannot be empty')
            return False
        if username == '':
            print('Username cannot be empty')
            return False
        if self.isAdmin and not self.db.findUser(username):
            print('User does not exist')
            return False

        if self.loginstatus:
            self.db.updateUser(username, {'password': self.hash_password(newpassword)})
            return True
        else:
            return False

    def showUsers(self):
        if not self.isAdmin:
            raise Exception('You are not an admin')

        users = self.db.findAll()
        print("\tAll users:")
        for user in users:
            print("\t\t",user['username'])

    def __del__(self):
        del self.db
