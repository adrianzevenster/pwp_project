import unittest
import idealModule as iM
import sys


class MyTestCase(unittest.TestCase):
    def test_shapes(self):

        self.results = iM.dataanalysis().data_shapes()
        self.expected = (400, 5)
        self.assertEqual(self.expected == self.expected)


if __name__ == '__main__':
    unittest.main()
