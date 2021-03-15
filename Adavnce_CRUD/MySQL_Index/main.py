"""
@Author: Ritika Patidar
@Date: 2021-03-15 00:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 00:10:38  
@Title : main code of perform index operation 
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from Mysql_Index import Index_Operation

def main():
    """
    Description:
        this function is define for mode of different operation of index
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Index_Operation=Index_Operation()
        mode=int(input("================================= Select Mode For index =====================================\n0 : Create Index\n====================================\n1 : Explain Index\n==============================================\n2 : Show Index\n==================================================================\n3 : Drop Index\n=============================================\n4 : quit\n=================================================================\nenter : "))
        if(mode==0):
            print(Obj_Index_Operation.Create_Index())
        elif(mode==1):
            print(Obj_Index_Operation.Explain_Index())
        elif(mode==2):
            Obj_Index_Operation.Show_Index()
        elif(mode==3):
            print(Obj_Index_Operation.Drop_Index())
        elif(mode==4):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()