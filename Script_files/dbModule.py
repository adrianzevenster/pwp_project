from sqlalchemy import create_engine
import pandas as pd
import os
import sys

print(sys.version_info)

"""
Variable initialization that acts as interface:
- directory: Project directory
- user_input_A: Training data(A) file name
- user_input_B: Testing data(B) file name
- user_input_C: Ideal data(C) file name
"""

directory = str("<directory_path>")
user_input_A = str("<file_name>")
user_input_B = str("<file_name>")
user_input_C = str("<file_name>")


class dbCreate:

    # static method to create database
    @staticmethod
    def database_creation(engine=create_engine("sqlite:///PwP_task_IUBH")):
        engine.execute("CREATE DATABASE PwP_Project")
        engine.execute("USE PwP_Project")

    def __init__(self):
        try:
            training_csv = pd.read_csv(os.path.join(directory, user_input_A))
        except IOError as e:
            print(e)
        try:
            testing_csv = pd.read_csv(os.path.join(directory, user_input_B))
        except IOError as e:
            print(e)
        try:
            ideal_csv = pd.read_csv(os.path.join(directory, user_input_C))
        except IOError as e:
            print(e)

        self.engine = create_engine("sqlite:///PwP_task_IUBH.db")
        self.engine.connect()
        self.training = pd.DataFrame(data=training_csv)
        self.testing = pd.DataFrame(data=testing_csv)
        self.ideal = pd.DataFrame(data=ideal_csv)



    def create_tables(self):
        """Creating tables in Database"""

        ''' training table creation'''
        self.training.to_sql(con=self.engine, name='trainingtable', if_exists='replace', index=False)

        '''ideal table creation'''
        self.ideal.to_sql(con=self.engine, name='idealtable', if_exists='replace', index=False)

        return 'Databases table creation for: training, ideal data has been created successfully'

    def update_tables(self, testing_results):
        """Creating table for test mapping results: <testModule.py"""
        testing_results.to_sql(con=self.engine, name='testingtable', if_exists='replace', index_label=False)

    def sql_query_training(self):
        """Training sql query function"""
        # sql query statement variable: <sql_statement_training>
        sql_statement_training = "SELECT * FROM trainingtable"
        training_sql = pd.read_sql_query(sql_statement_training, self.engine)
        return training_sql

    def sql_query_testing(self):
        """Testing sql query function"""
        # sql query statement variable: <sql_statement_testing>
        sql_statement_testing = "SELECT * FROM testingtable"
        testing_sql = pd.read_sql_query(sql_statement_testing, self.engine)
        return testing_sql

    def sql_query_ideal(self):
        """Ideal query function"""
        # sql query statement: <sql_statement_ideal>
        sql_statement_ideal = "SELECT * FROM idealtable"
        ideal_sql = pd.read_sql_query(sql_statement_ideal, self.engine)
        return ideal_sql

