import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from app.app import get_coords
import unittest

class TestApp(unittest.TestCase):
    def test01_check_correct_city(self):
        coords = get_coords("Bengaluru")
        self.assertEqual(coords, (12.97623, 77.603287))

    def test02_check_incorrect_city(self):
        coords = get_coords("Bangalore")
        self.assertNotEqual(coords, (12.97623, 77.603287))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestApp))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
