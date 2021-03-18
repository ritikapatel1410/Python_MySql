"""
@Author: Ritika Patidar
@Date: 2021-03-18 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-18 00:10:38  
@Title : main code of perform window analytical function on table
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from MySQL_Analytical_Function import Analytical_Function

def main():
    """
    Description:
        this function is define for mode of show the functionality of window Analytical_Function
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Analytical_Function=Analytical_Function()
        mode=int(input("================================= Select Mode For Analytical Function =====================================\n0 : Ntile\n====================================\n1 : Lead\n==============================================\n2 : Lag\n==================================================================\n3 : First Value Function\n=============================================\n4 : Last Value Function\n==============================================\n5 : quit\n=====================\nenter: "))
        if(mode==0):
            Obj_Analytical_Function.NTILE_Function()
        elif(mode==1):
            Obj_Analytical_Function.LEAD_Function()
        elif(mode==2):
            Obj_Analytical_Function.LAG_Function()
        elif(mode==3):
            Obj_Analytical_Function.FIRST_VALUE_Function()
        elif(mode==4):
            Obj_Analytical_Function.LAST_VALUE_Function()
        elif(mode==5):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()