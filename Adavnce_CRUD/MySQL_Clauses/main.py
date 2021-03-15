"""
@Author: Ritika Patidar
@Date: 2021-03-13 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-13 10:10:38  
@Title : main code for perform mysql clause on table
"""

from mysql_clause import clause
import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
from input_file import Input_clause

def main():
    try:
        Obj_clause=clause()
        obj_Input_clause=Input_clause()
        mode=int(input("===================================================select mode for clause of table ====================================================\n0 : clause where\n====================================\n1 : clause distinct\n==============================================\n2 : clause form\n==================================================================\n3 : clause orderby\n=============================================\n4 : clause groupby\n===========================================================\n5 : quit\n================================================================\nenter : "))
        if(mode==0):
            table_name,condition=obj_Input_clause.input_function("clause_where")
            print(Obj_clause.clause_where(table_name,condition))
        elif(mode==1):
            table_name,column=obj_Input_clause.input_function("clause_distinct")
            print(Obj_clause.clause_distinct(table_name,column))
        elif(mode==2):
            print(Obj_clause.clause_form(obj_Input_clause.input_function("clause_form")))
        elif(mode==3):
            table_name,condition,order_by_condition=obj_Input_clause.input_function("clause_orderby")
            Obj_clause.clause_orderby(table_name,condition,order_by_condition)
        elif(mode==4):
            table_name,condition,group_by_condition=obj_Input_clause.input_function("clause_groupby")
            Obj_clause.clause_groupby(table_name,condition,group_by_condition)
        elif(mode==5):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))


main()