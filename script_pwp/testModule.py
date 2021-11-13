import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from idealModule import dataanalysis
from idealModule import IdealFunc
import seaborn as sns
import dbModule as db


class testingFunc(IdealFunc):

    def __init__(self):
        super().__init__()
        self.training = self.training
        self.ideal = self.ideal
        self.ideal_function = self.ideal_function()
        self.testing = db.dbCreate().testing

    def testing_function(self):
        self.mapping_testing = []

        for i in range(self.testing.shape[0]):
            for k in self.ideal_function.keys():
                fn_ideal = self.ideal_function[k][0]
                max_dev = self.ideal_function[k][1]
                index = np.where(self.ideal["x"] == self.testing.iloc[i][0])
                dev = np.absolute(np.subtract(self.testing.iloc[i][1], self.ideal[fn_ideal].iloc[index].to_numpy()))
                if np.sqrt(2) * max_dev > dev[0]:
                    self.mapping_testing.append((self.testing.iloc[i][0], self.testing.iloc[i][1], fn_ideal, dev[0]))
        return self.mapping_testing

    def testing_results_dataframe(self):
        self.testing_results = testingFunc().testing_function()
        '''Converting testing_results <list> to testing_results_df <dataframe>
        - allow for column names to be added'''

        self.testing_results_df= pd.DataFrame(self.testing_results, columns=['testing_x',
                                                                              'testing_Yn',
                                                                              'ideal_function',
                                                                              'deviation'])
        return self.testing_results_df

    def testing_visualization(self):
        self.testing_visualization = testingFunc().testing_results_dataframe()
        plt.plot(self.testing_visualization['testing_x'], self.testing_visualization['testing_Yn'])
        sns.lmplot(x='testing_x', y='testing_Yn', hue='deviation', data=self.testing_visualization)
        plt.show()

p = testingFunc()
print(p.testing_function())

'''
class testingVisualization:
    def __init__(self):
        self.testing_results = testingFunc().testing_function()

    def testing_visualization(self):
        self.testing_results = testingFunc().testing_function()
        print(self.testing_results)

'''


