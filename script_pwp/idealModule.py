import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
import dbModule as db



class dataanalysis:
    def __init__(self):
        """ Class for basic data analysis"""
        db_import = db.dbCreate()
        self.training = db_import.sql_query_training()
        self.testing = db_import.sql_query_testing()
        self.ideal = db_import.sql_query_ideal()



    def print_head(self, rows):
        print(self.training.head(rows))

    def sum_stats(self):
        """Summary statistics of Data"""
        return 'Summary statistics\nTraining: \n{}\n Testing: \n{} \nIdeal: \n{}'.format(self.training.describe(),
                                                                                         self.testing.describe(),
                                                                                         self.ideal.describe())

    def stand_dev(self):
        standard_dev = {'training std': self.training.std(), 'ideal std': self.ideal.std()}
        return standard_dev

    def data_shapes(self):
        return "DataFrame Shapes(rows, columns):\nTraining: {}\nTesting: {}\nIdeal:".format(self.training.shape,
                                                                                            self.testing.shape,
                                                                                            self.ideal.shape)

    def data_types(self):
        if type(self.training) != float:
            self.training = self.training.convert_dtypes(float)

        elif type(self.testing) != float:
            self.testing = self.testing.convert_dtypes(float)
        elif type(self.ideal) != float:
            self.ideal = self.ideal.convert.dtypes(float)
        else:
            print("All DataFrames are floats")

        return self.training.dtypes, self.testing.dtypes, self.ideal.dtypes

    def linear_plots(self):
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(self.ideal['x'],
                self.ideal[[i for i in self.ideal if i != 'x']],
                alpha=0.4, )
        ax.plot(self.training['x'],
                self.training[[i for i in self.training if i != 'x']],
                alpha=0.3,
                label=f'{self.training}')
        ax.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Testing data and Training data")
        plt.show()

    def seperate_plots(self):
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

    def pairplot(self):
        sns.pairplot(self.ideal)
        plt.show()




class IdealFunc(dataanalysis):
    def __init__(self):
        super().__init__()

    def ideal_function(self):
        self.ideal_function_df = pd.DataFrame(data=None)
        for i_col in self.training.columns[1:]:
            least_square_error = sys.maxsize
            for i_icol in self.ideal.columns[1:]:
                dev = np.absolute(np.subtract(self.training[i_col].to_numpy(), self.ideal[i_icol].to_numpy()))
                # std_dev = np.absolute(dev/len(dev))
                lse = np.sum(np.square(dev))
                if lse < least_square_error:
                    least_square_error = lse
                    self.ideal_function_df[i_col] = (i_icol, dev.max(), least_square_error)
        return self.ideal_function_df

    def ideal_function_visualization(self):
        self.ideal_funcion_results = IdealFunc().ideal_function()
        for col in self.training.columns[1:]:
            ideal_fn = self.ideal_funcion_results[col][0]
            plt.scatter(self.training['x'], self.training[col], label=f' Training {col}', alpha=0.6)
            plt.scatter(self.ideal['x'], self.ideal[ideal_fn], label=f' Ideal {ideal_fn}', alpha=0.2)
            plt.title("Ideal Function vs Training Function")
            plt.legend()
            plt.show()


