import os
import unittest
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from app.db import DB

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB()

    def test1_db_init(self):
        self.assertIsInstance(self.db, DB)

    def test2_db_get_all_users(self):
        self.assertIsInstance(self.db.findAll(), list)

    def test3_db_get_user_by_username(self):
        self.assertIsInstance(self.db.findUser('admin'), dict)

    def test4_insert_user(self):
        self.assertIsNone(self.db.insertUser(username='admin3', password='admin3', role='admin'))

    def test5_update_user(self):
        self.assertIsNone(self.db.updateUser('admin3', {'username': 'admin2', 'password': 'admin2', 'role': 'admin'}))

    def test6_delete_user(self):
        self.assertIsNone(self.db.deleteUser('admin2'))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDB))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
