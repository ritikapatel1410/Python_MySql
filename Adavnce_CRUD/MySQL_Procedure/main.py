"""
@Author: Ritika Patidar
@Date: 2021-03-15 23:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 23:10:38  
@Title : main code of perform store procedure operation
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from Mysql_Procedure import Procedure_Operation

def main():
    """
    Description:
        this function is define for mode of different operation on store procedure
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Procedure_Operation=Procedure_Operation()
        mode=int(input("================================= Select Mode Of Procedure =====================================\n0 : Create Procedure\n====================================\n1 : Show Procedure\n==============================================\n2 : Status Procedure\n==================================================================\n3 : Drop Procedure\n=============================================\n4 : quit\n=================================================================\nenter : "))
        if(mode==0):
            print(Obj_Procedure_Operation.Create_Procedure())
        elif(mode==1):
            print(Obj_Procedure_Operation.Show_Procedure())
        elif(mode==2):
            Obj_Procedure_Operation.Status_Procedure()
        elif(mode==3):
            print(Obj_Procedure_Operation.Drop_Procedure())
        elif(mode==4):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()