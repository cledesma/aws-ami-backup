# test suite should be run from the root: python test/main_test_suite.py
import sys
sys.path.append('src') 
import unittest
from main import Main

class MainTestSuite(unittest.TestCase):

	def test(self):
		main = Main()
		self.assertEqual(main.demotest(), 2)

if __name__ == '__main__':
    unittest.main()