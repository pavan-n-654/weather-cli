import unittest
import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from app.user import User

class TestUser(unittest.TestCase):
    def setUp(self): 
        self.user1 = User('admin')
        self.user2 = User('user')
        self.user3 = User('notAuser')

    def test01_admin_login_success(self):
        self.assertTrue(self.user1.login('password'))

    def test02_add_user_success(self):
        self.user1.login('password')
        self.user1.addUser('user', 'password')
        self.assertTrue(self.user1.db.findUser('user').get('username', 'test')=='user')

    def test03_user_login_success(self):
        self.assertTrue(self.user2.login('password'))

    def test04_user_login_wrong_password(self):
        self.assertFalse(self.user2.login('wrongpassword'))

    def test05_non_existent_user_login(self):
        self.assertFalse(self.user3.login('password'))

    def test06_add_user_failure_no_password(self):
        self.user1.login('password')
        self.assertFalse(self.user1.addUser('user2', ''))

    def test07_add_user_failure_no_username(self):
        self.user1.login('password')
        self.assertFalse(self.user1.addUser('', 'password'))

    def test08_add_user_failure_no_username_no_password(self):
        self.user1.login('password')
        self.assertFalse(self.user1.addUser('', ''))

    def test09_add_user_failure_existing_username(self):
        self.user1.login('password')
        self.assertFalse(self.user1.addUser('admin', 'password'))

    def test10_find_single_user_success(self):
        self.user1.login('password')
        self.assertTrue(self.user1.db.findUser('admin')['username']=='admin')

    def test11_find_single_user_failure(self):
        self.user1.login('password')
        self.assertFalse(self.user1.db.findUser('notAuser'))

    def test12_find_all_users_success(self):
        self.user1.login('password')
        # only admin,user should be in the list
        self.assertTrue(len(self.user1.db.findAll())==2)

    def test13_fail_login_after_loging_in(self):
        temp_user = User('user')
        status = temp_user.login('password')
        self.assertFalse(temp_user.login('password'))
        del temp_user

    def test14_delete_user_success(self):
        self.user1.login('password')
        self.user1.deleteUser('user')
        self.assertFalse(self.user1.db.findUser('user'))

    def test15_delete_user_failure(self):
        self.user1.login('password')
        self.assertFalse(self.user1.deleteUser('notAuser'))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUser))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    exit(0)
