'''
@Author: Ritika Patidar
@Date: 2021-03-12 13:50:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-12 13:50:38  
@Title : main code of perform basic curd operation on table
'''
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from input_file import Input_CRUD
from Basic_CRUD_table import Basic_CRUD

def main():
    Obj_Basic_CRUD=Basic_CRUD()
    Obj_Input_CRUD=Input_CRUD()
    try:
        mode=int(input("================================ enter the mode of table operation ====================================\n0 : create table\n===============================\n1 : insert data\n===========================================\n2 : show records\n=================================\n3 : delete records\n======================================\n4 : add column table\n==========================================\n5 : update data\n==============================================\n6 : quit\n======================================\nenter mode: "))
        loggerfile.Logger("info","successfully mode selected")
        if(mode==0):
            Obj_Basic_CRUD.create_table(Obj_Input_CRUD.input_function("create_table"))
        elif(mode==1):
            table_name,val,field_names=Obj_Input_CRUD.input_function("insert_data")
            Obj_Basic_CRUD.insert_data(table_name,val,field_names)
        elif(mode==2):
            Obj_Basic_CRUD.show_records(Obj_Input_CRUD.input_function("show_records"))
        elif(mode==3):
            table_name,column,column_value=Obj_Input_CRUD.input_function("delete_records")
            Obj_Basic_CRUD.delete_records(table_name,column,column_value)
        elif(mode==4):
            table_name,column_name,dtype=Obj_Input_CRUD.input_function("add_column_table")
            Obj_Basic_CRUD.add_column_table(table_name,column_name,dtype)
        elif(mode==5):
            table_name,update_data,update_condition=Obj_Input_CRUD.input_function("update_data")
            Obj_Basic_CRUD.update_data(table_name,update_data,update_condition)
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))

main()