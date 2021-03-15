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
from Mysql_view import View_Operation

def main():
    """
    Description:
        this function is define for mode of different operation on view
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_View_Operation=View_Operation()
        mode=int(input("================================= Select Mode For View =====================================\n0 : Create View\n====================================\n1 : Update View\n==============================================\n2 : Show View\n==================================================================\n3 : Drop View\n=============================================\n4 : quit\n=================================================================\nenter : "))
        if(mode==0):
            print(Obj_View_Operation.Create_View())
        elif(mode==1):
            print(Obj_View_Operation.Update_View())
        elif(mode==2):
            Obj_View_Operation.Show_View()
        elif(mode==3):
            print(Obj_View_Operation.Drop_View())
        elif(mode==4):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()