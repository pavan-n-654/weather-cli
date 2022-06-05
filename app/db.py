import pymongo
import os

class DB:
    def __init__(self):
        """
        Initializes the DB class
        :return: None
        """
        self.conn = pymongo.MongoClient(os.environ.get('DB_HOST', 'localhost'), os.environ.get('DB_PORT', 27017))
        self.db = self.conn[os.environ.get('DB_NAME', 'test')]
        self.collection = self.db[os.environ.get('DB_COLLECTION', 'test')]

    def insertUser(self, username, password):
        """
        Inserts a new document into the collection
        :param username: The username of the user
        :param password: The password of the user
        :return: None
        """
        self.collection.insert_one({'username': username, 'password': password})

    def findAll(self):
        """
        Finds all Users in the collection
        :return: A list of all users
        """
        return self.collection.find()

    def findUser(self, username, password):
        """
        Finds a user in the collection
        :param username: The username of the user
        :param password: The password of the user
        :return: The user if found, None otherwise
        """
        return self.collection.find_one({'username': username, 'password': password})

    def updateUser(self, username, new_data):
        """
        Updates a user in the collection
        :param username: The username of the user
        :param new_data: dict of new data with keys username and/or password
        :return: None
        """
        self.collection.update_one({'username': username}, {'$set': new_data})

    def delete(self, username):
        """
        Deletes a user from the collection
        :param username: The username of the user
        :return: None
        """
        self.collection.delete_one({'username': username})
