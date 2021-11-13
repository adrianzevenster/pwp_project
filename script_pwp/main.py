import dbModule as db
import idealModule as iM
import testModule as tM

"""
Class and method calls for db.Module.py
"""
dataBase = db.dbCreate()

print(iM.dataanalysis().data_shapes())


"""
Class and method calls for idealModule.py
"""
idealModule_dataAnalysis = iM.dataanalysis()
idealModule_IdealFunction = iM.IdealFunc()


"""
Class and Method calls for testModule.py
"""
testModule = tM.testingFunc()
testModule_testingFunction = tM.testingFunc()
print(testModule_testingFunction.testing_results_dataframe())

dataBase.update_tables(testModule_testingFunction.testing_results_dataframe())