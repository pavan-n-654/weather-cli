import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import test_user
import test_db
import pymongo
from hashlib import sha256


conn = pymongo.MongoClient("localhost", 27017)
if conn["test"] != None: conn.drop_database("test")
db = conn["test"]
collection = db["test"]

collection.insert_one({"username": "admin", "password": sha256("password".encode('utf-8')).hexdigest(), "role": "admin"})

AllSuite = unittest.TestSuite([
    test_db.suite(),
    test_user.suite()
    ])
unittest.TextTestRunner(verbosity=2).run(AllSuite)

