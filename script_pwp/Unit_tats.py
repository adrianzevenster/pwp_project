import idealModule as iM
import pandas as pd
import unittest
training_csv = pd.read_csv("C:/Users/CustomBeast/PycharmProjects/PwP_Project/test.csv")
training_pd = pd.DataFrame(training_csv)

def data_shape(data):
    return data.shape


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.df = training_csv
    def testExample(self):
        results = data_shape(self.df)
        self.assertEqual(results, (400, 5), "dataFrame is not the correct shape")

if __name__ == "__main__":
    unittest.main()