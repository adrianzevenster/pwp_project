import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import dbModule as db
from bokeh.plotting import figure, save, show

"""
Class for dataAnalysis, methods include data descriptions(1), preprocessing(2), and visualization(3)
- test_null_values: Checks dataset(s) [A, B, C] for null values: unittest (1 & 2)
- sum_stats: Summary statistics on all datasets (1)
- stand_dev: Return standard deviation of column in datasets [A, C] (1)
- data_shapes: Return shapes of all datasets (1)
- data_types: Check data types of all datasets, if type not appropriate: converts to <float> (1 & 2)
- Linear_plots: Visualization of datasets [A, C]
- separate_plots: Visualization of datasets[A, C]
"""


class dataAnalysis:

    def __init__(self):
        """ Class for basic data analysis"""
        db_import = db.dbCreate()
        self.training = db_import.training  # db_import.sql_query_training()
        self.testing = db_import.testing
        self.ideal = db_import.sql_query_ideal()


    def test_null_values(self):
        """TDD for testing null values"""
        training, testing, ideal = self.training, self.testing, self.ideal
        if training is None:
            return training
        elif testing is None:
            return testing
        elif ideal is None:
            return ideal
        else:
            print("Dataset(s) has no null values")

    def sum_stats(self):
        """Summary statistics of Data"""
        return "Summary_statistics:" \
               'Training', self.training.describe(), \
               'Testing', self.testing.describe(), \
               'Ideal', self.ideal.describe()

    def stand_dev(self):
        """Pandas standard deviation function: return <str>"""

        standard_dev = {'training std': self.training.std(), 'ideal std': self.ideal.std()}
        return standard_dev

    def covariance(self):
        return self.training.cov()

    def data_shapes(self):
        return "Data Shapes:", \
               'Training', self.training.shape, \
               'Testing', self.testing.shape, \
               'Ideal', self.ideal.shape

    def data_types(self):
        """Preprocessing: Data type check and conversion: <float>"""
        if type(self.training) != float:
            self.training = self.training.convert_dtypes(float)

        elif type(self.testing) != float:
            self.testing = self.testing.convert_dtypes(float)
        elif type(self.ideal) != float:
            self.ideal = self.ideal.convert.dtypes(float)
        else:
            print("All DataFrames are floats")
        return self.training, self.testing, self.ideal

    def linear_plots(self):
        """
        Data Visualization: Training[A], Ideal[C]
        - Superimposed representation
        """
        fig, ax = plt.subplots(figsize=(10, 4))
        '''Training data[A] plot'''
        ax.plot(self.ideal['x'],
                self.ideal[[i for i in self.ideal if i != 'x']],
                alpha=0.4, )
        '''Ideal data[C] plot'''
        ax.plot(self.training['x'],
                self.training[[i for i in self.training if i != 'x']],
                alpha=0.3,
                label=f'{self.training}')
        ax.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Testing data and Training data")
        plt.show()

    def separate_plots(self):
        """
        Separate Visualization representation
        - ax1:Training data[A]
        - ax2:Ideal data[C]
        """
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(self.training['x'],
                 self.training[[i for i in self.training if i != 'x']],
                 alpha=0.9)
        ax2.plot(self.ideal['x'],
                 self.ideal[[i for i in self.ideal if i != 'x']],
                 alpha=0.9)
        ax1.set_title("Training data")
        ax2.set_title("Testing data")
        ax1.set_xlabel("x-value")
        ax1.set_ylabel("y-values(s)")
        ax1.legend(self.training.columns[1:].values)
        ax2.set_xlabel("x-value")
        ax2.set_ylabel("y_values(s)")
        ax2.legend(self.ideal.columns[1:].values, loc='best', ncol=5)
        plt.show()


"""
Class to determine ideal function <-- dataAnalysis
"""


class IdealFunc(dataAnalysis):
    """IdealFunc inheritance from dataAnalysis"""

    def __init__(self):
        super().__init__()
        # Ideal function storing variable: <pd.DataFrame>
        self.ideal_function_df = pd.DataFrame(data=None)
        self.ideal_function_df = self.ideal_function()

    def ideal_function(self):
        """Method to determine ideal function: return <pd.DataFrame>"""
        for i_col in self.training.columns[1:]:
            least_square_error = sys.maxsize
            for i_icol in self.ideal.columns[1:]:
                # dev: calculation of y-value deviation between training and ideal data
                dev = np.absolute(np.subtract(self.training[i_col].to_numpy(), self.ideal[i_icol].to_numpy()))
                std_dev = dev / len(self.ideal)

                # sum of squares calculated for <dev>
                lse = np.absolute(np.sum(np.square(std_dev)))
                if lse < least_square_error:
                    '''finding the value the function that minimizes the y-deviation'''
                    least_square_error = lse
                    # Ideal function results: training column = (ideal column, maximum deviation, least square value)
                    self.ideal_function_df[i_col] = (i_icol, dev.max(), least_square_error)
        return self.ideal_function_df

    def ideal_function_visualization_bokeh(self):

        for col in self.training.columns[1:]:
            ideal_function_col = self.ideal_function_df[col][0]
            ideal_graph = figure(title=f'Ideal Function[{ideal_function_col}] vs 'f'Training Function[{col}]')
            ideal_graph.scatter(self.ideal['x'], self.ideal[ideal_function_col], color='purple', alpha=0.6,
                                legend_label=f'Ideal function{ideal_function_col}')
            ideal_graph.scatter(self.training['x'], self.training[col], color='turquoise', alpha=0.6,
                                legend_label=f'Training function{col}')
            ideal_graph.legend.location = 'top_right'
            ideal_graph.legend.click_policy = 'hide'
            save(ideal_graph)
            show(ideal_graph)