"""
@Author: Ritika Patidar
@Date: 2021-03-15 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 10:10:38  
@Title : main code of perform join operation on tables
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from Mysql_join import JOIN

def main():
    """
    Description:
        this function is define for mode of different type of join
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_JOIN=JOIN()
        mode=int(input("================================= Select Mode For MySQL Join =====================================\n0 : Inner Join\n====================================\n1 : Left Join\n==============================================\n2 : Right Join\n==================================================================\n3 : Full Join\n=============================================\n4 : quit\n=================================================================\nenter : "))
        if(mode==0):
            Obj_JOIN.Inner_Join()
        elif(mode==1):
            Obj_JOIN.Left_Join()
        elif(mode==2):
            Obj_JOIN.Right_Join()
        elif(mode==3):
            Obj_JOIN.Full_Join()
        elif(mode==4):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()