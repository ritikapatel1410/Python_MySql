"""
@Author: Ritika Patidar
@Date: 2021-03-13 0:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-13 10:10:38  
@Title : main code perform basic curd operation on database
"""

from Basic_CRUD_database import Basic_CRUD_DB, input_database
import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile

def main():
    #while True:
    try:
        Basic_CRUD_DB_OBJ=Basic_CRUD_DB()
        mode=int(input("===================================================select mode of database====================================================\n===============================\n0 : create database\n====================================\n1 : show databases\n==============================================\n2 : drop database\n==================================================================\n3 : quit\n===============================================================\nenter: "))
        if(mode==0):
            print(Basic_CRUD_DB_OBJ.create_db(input_database()))
        elif(mode==1):
            print(Basic_CRUD_DB_OBJ.show_list_of_db())
        elif(mode==2):
            print(Basic_CRUD_DB_OBJ.drop_db(input_database()))
        elif(mode==3):
            sys.exit()
        loggerfile.Logger("info","succesfully select the mode")
        #break
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))


main()