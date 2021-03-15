"""
@Author: Ritika Patidar
@Date: 2021-03-15 23:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 23:10:38  
@Title : main code of perform view operation
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from Mysql_import_export import Import_Export

def main():
    """
    Description:
        this function is define for mode of import export operation
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Import_Export=Import_Export()
        mode=int(input("================================= Select Mode For Import and Export Operation =====================================\n0 : Export table \n====================================\n1 : Import Table\n==============================================\n2 : quit\n===============================================\nenter : "))
        if(mode==0):
            try:
                export_mode=int(input("==================================\n0 : Export Table in csv file\n=================================\n1 : Export Table in excel sheet\n====================================\n2 : quit \n==========================\nenter: "))
                if(export_mode==0):
                   print(Obj_Import_Export.Export_table_csv()) 
                elif(export_mode==1):
                   print(Obj_Import_Export.Export_table_excel())
                elif(export_mode==2):
                    sys.exit()   
            except Exception as error:
                loggerfile.Logger("error","{0} error occured".format(error))
        elif(mode==1):
            print(Obj_Import_Export.Import_Table_csv())
        elif(mode==2):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()