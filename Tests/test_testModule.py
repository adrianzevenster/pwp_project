import unittest
import testModule as tM


class TestTestFunc(unittest.TestCase):
    def setUp(self):
        """Set up variables for testing of testModule.py module"""
        # Testing mapping results: <pd.DataFrame>
        self.testing_results = tM.testingFunc().testing_results_dataframe()
        # Ideal function results: <pd.DataFrame>
        self.ideal_function = tM.testingFunc().ideal_function
        # Testing data(B): <pd.DataFrame>
        self.testing = tM.testingFunc().testing

    def test_if_test_results(self):
        """Test for instance of testing results: <pd.DataFrame>"""
        if self.testing_results is not None:
            self.test_testResults_instance = True
            return self.test_testResults_instance
        self.assertNotIsInstance(self.test_testResults_instance, True, "There is no <pd.DataFrame>: Testing Results")

    def test_column_names(self):
        """Testing for expected column names in testing results"""
        results = list(self.testing_results.columns)
        expected = ['testing_x', 'testing_Yn', 'ideal_function', 'deviation']
        self.assertListEqual(results, expected, "columns are not as expected in testing results dataFrame")

    def testing_data_shape(self):
        """Test if testing data(B) has correct shape"""
        result = self.testing.shape
        self.assertEqual(result, (400, 5), "Testing data does not have expected shape")

    def test_for_string(self):
        """Test to ensure ideal function is represented in testing results"""
        expected = type(self.testing_results.iloc[:, 2])
        self.assertTrue(expected, "str")


if __name__ == '__main__':
    unittest.main()
