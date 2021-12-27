import unittest
import idealModule as iM
import dbModule as db


class TestdbCreate(unittest.TestCase):
    """Testing that database connection is present"""
    class testDbConnetion(unittest.TestCase):
        connection = None

        def setUp(self):
            # set up database connection from dbModule.py
            self.dBase = db.dbCreate()
            self.db_connection = self.dBase.engine.connect()
            self.analysisClass = iM.dataAnalysis()

        def tearDown(self):
            # check for database instance
            if self.db_connection is not None and self.db_connection:
                self.db_connection.close()
            else:
                return "database connection unsuccessful"


class TestidealFunction(unittest.TestCase):
    def setUp(self):
        """Declaring class object as attributes"""
        self.analysisClass = iM.dataAnalysis()
        self.idealFuncClass = iM.IdealFunc()

    def test_test_null_values(self):
        """ TDD - Testing for null values: dataAnalysis"""
        # check if any dataframes in dataAnalysis for null values
        if self.analysisClass.test_null_values():
            expected_message = "Null values are present"
            self.assertEqual(expected_message)

    def test_type(self):
        """Test to determine if all dataset types are as expected: <pd.DataFrame>"""
        train = type(self.analysisClass.training)
        ideal = type(self.analysisClass.ideal)
        self.assertIs(train, ideal, "This is not the same")

    def test_columns(self):
        """Test to determine if training function columns are presents in ideal function: y1, y2, y3, y4"""
        train_col = list(self.analysisClass.training.columns[1:])
        test_col = list(self.idealFuncClass.ideal_function().columns)
        self.assertListEqual(train_col, test_col)

    def test_ideal_function_results_columns(self):
        """Test to determine if 4(expected) ideal functions are returned"""
        test = self.idealFuncClass.ideal_function().columns
        expected = len(test)
        self.assertEqual(expected, 4)


if __name__ == '__main__':
    unittest.main()
