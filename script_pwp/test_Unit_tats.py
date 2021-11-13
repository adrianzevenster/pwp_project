import unittest
import Unit_tats


class MyTestCase(unittest.TestCase):
    def test_func(self):
        results = Unit_tats.func(10, 5)
        self.assertEqual(results, 1)


'''

This tells you to run the code inside the conditional
'''
if __name__ == '__main__':
    unittest.main()
