"""
@Author: Ritika Patidar
@Date: 2021-03-15 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 10:10:38  
@Title : main code of perform window aggregate function on table
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from MySQL_Aggregate_Function import Aggregate_Function

def main():
    """
    Description:
        this function is define for mode of show the functionality of Aggregate Function
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Aggregate_Function=Aggregate_Function()
        mode=int(input("================================= Select Mode For Aggregate Function =====================================\n0 : Count\n====================================\n1 : Sum\n==============================================\n2 : AVG\n==================================================================\n3 : Min\n=============================================\n4 : Max\n===========================================================\n5 : First Value\n================================================================\n6 : Last Value\n=====================\n7 : quit\n=====================\nenter: "))
        if(mode==0):
            Obj_Aggregate_Function.Count_Fuction()
        elif(mode==1):
            Obj_Aggregate_Function.Sum_Fuction()
        elif(mode==2):
            Obj_Aggregate_Function.AVG_Fuction()
        elif(mode==3):
            Obj_Aggregate_Function.Min_Fuction()
        elif(mode==4):
            Obj_Aggregate_Function.Max_Fuction()
        elif(mode==5):
            print(Obj_Aggregate_Function.First_Fuction())
        elif(mode==6):
            print(Obj_Aggregate_Function.Last_Fuction())
        elif(mode==7):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()