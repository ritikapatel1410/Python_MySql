"""
@Author: Ritika Patidar
@Date: 2021-03-15 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 10:10:38  
@Title : main code of perform window ranking function on table
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from MySQL_Ranking_Function import Ranking_Function

def main():
    """
    Description:
        this function is define for mode of show the functionality of window Ranking Function
    Parameter:
        None
    Return:
        None
    """
    try:
        Obj_Ranking_Function=Ranking_Function()
        mode=int(input("================================= Select Mode For Ranking Function =====================================\n0 : Rank\n====================================\n1 : Dense Rank\n==============================================\n2 : Percentage Rank\n==================================================================\n3 : Row number\n=============================================\n4 : Dist Rank\n==============================================\n5 : quit\n=====================\nenter: "))
        if(mode==0):
            Obj_Ranking_Function.RANK_Fuction()
        elif(mode==1):
            Obj_Ranking_Function.DENSE_RANK_Fuction()
        elif(mode==2):
            Obj_Ranking_Function.PERCENT_RANK_Fuction()
        elif(mode==3):
            Obj_Ranking_Function.ROW_NUMBER_Fuction()
        elif(mode==4):
            Obj_Ranking_Function.CUME_DIST()
        elif(mode==5):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

    
main()