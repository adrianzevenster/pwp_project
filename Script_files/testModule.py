import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from idealModule import IdealFunc
import dbModule as db


class testingFunc(IdealFunc):
    """Testing mapping with inheritance from IdealFunc Class"""

    def __init__(self):
        super().__init__()
        # Declaring variable containing the Ideal Function:<pd.DataFrame>.
        self.ideal_function = self.ideal_function_df
        self.mapping_testing = []
        self.mapping_testing = self.testing_function()
        self.test_results = self.testing_results_dataframe()

    def testing_function(self):
        """Mapping of testing data to ideal function: <list>"""
        for i in range(self.testing.shape[0]):
            for k in self.ideal_function.keys():
                # ideal function column value from ideal data
                fn_ideal = self.ideal_function[k][0]
                # maximum deviation corresponding to ideal function
                max_dev = self.ideal_function[k][1]
                index = np.where(self.ideal["x"] == self.testing.iloc[i][0])
                # deviation calculation: subtracting ideal data containing ideal function from testing data
                dev = np.absolute(np.subtract(self.testing.iloc[i][1], self.ideal[fn_ideal].iloc[index].to_numpy()))
                if np.sqrt(2) * max_dev > dev:  # pow(dev, 2) < dev_max also works
                    '''Criteria for mapping test case to the ideal function'''
                    # List containing results from mapping criteria: <list>
                    self.mapping_testing.append((self.testing.iloc[i][0], self.testing.iloc[i][1], fn_ideal, dev[0]))
        return self.mapping_testing

    def testing_results_dataframe(self):
        """
        Converting testing_results <list> -> <pd.Dataframe>
        - Allows for column names be added
        """
        # Retrieve testing_function() method results
        self.testing_results_df = pd.DataFrame(self.mapping_testing, columns=['testing_x',
                                                                              'testing_Yn',
                                                                              'ideal_function',
                                                                              'deviation'])
        return self.testing_results_df

    def testing_visualization(self):
        """Visualize testing data [C] mapping to ideal function"""
        fig, axes = plt.subplots()
        axes.plot(self.test_results[['testing_Yn']], label="Testing Results", alpha=0.6)
        # Functions from ideal data that are present in ideal function: ideal_data[idea function columns]
        axes.plot(self.ideal[['y49', 'y39', 'y40',  'y4']], label='Ideal Function', alpha=0.9)
        plt.title("Test data(C) to Ideal Function Mapping")
        plt.legend()
        plt.show()

    def appending_results(self):
        """Appending test mapping results to database: idealTable"""
        test_append = db.dbCreate()
        # Method argument from dbCreate: update_tables(testing_results)
        test_append.update_tables(self.test_results)
        return "Test mapping results have been appended to database"
