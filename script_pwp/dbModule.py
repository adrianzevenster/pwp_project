from sqlalchemy import create_engine
import pandas as pd
import sys


"mysql+pymysql://root:a?xBVq1!@localhost"
class dbCreate:

    @staticmethod
    def dataBase_creation(engine=create_engine("sqlite:///PwP_task_IUBH")):
        engine.execute("CREATE DATABASE PwP_Project")
        engine.execute("USE PwP_Project")


    def __init__(self):
        training_csv = pd.read_csv(sys.argv[1])
        testing_csv = pd.read_csv(sys.argv[2])
        ideal_csv = pd.read_csv(sys.argv[3])
        self.engine = create_engine("sqlite:///PwP_task_IUBH.db")
        self.engine.connect()
        self.training = pd.DataFrame(data=training_csv)
        self.testing = pd.DataFrame(data=testing_csv)
        self.ideal = pd.DataFrame(data=ideal_csv)

    def create_tables(self):

        '''
        training table
        '''
        self.training.to_sql(con=self.engine, name='trainingtable', if_exists='replace', index=False)
        '''
        ideal data
        '''
        self.ideal.to_sql(con=self.engine, name='idealtable', if_exists='replace', index=False)

        return 'Databases table creation for: training, testing, ideal data has been created successfully'
    def update_tables(self, testing_results):
        testing_results.to_sql(con=self.engine, name='testingtable', if_exists='replace', index_label=False)

    def sql_query_training(self):
        '''
        Training table sql query
        '''

        # sql query statement variable: <sql_statement_training>
        sql_statement_training = "SELECT * FROM trainingtable"
        training_sql = pd.read_sql_query(sql_statement_training, self.engine)
        return training_sql

    def sql_query_testing(self):
        # sql query statement variable: <sql_statement_testing>
        sql_statement_testing = "SELECT * FROM testingtable"
        testing_sql = pd.read_sql_query(sql_statement_testing, self.engine)
        return testing_sql
    '''
    ideal data query function
    '''
    def sql_query_ideal(self):
        # sql query statement: <sql_statement_ideal>
        sql_statement_ideal = "SELECT * FROM idealtable"
        ideal_sql = pd.read_sql_query(sql_statement_ideal, self.engine)
        return ideal_sql

