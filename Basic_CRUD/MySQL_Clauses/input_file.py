'''
@Author: Ritika Patidar
@Date: 2021-03-15 9:06:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 9:06:38  
@Title : code for perform mysql clause on table
'''
import mysql.connector as mysql 
from decouple import config
import time
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile

class Input_clause:
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()

    def input_function(self,return_type):
        if(return_type=="clause_where"):
            table_name=input("=======================\nenter table name: ")
            self.mycursor.execute("SHOW COLUMNS FROM "+table_name)
            column_list=[[column[0],str(str(column[1]).split("'")[1]).split("(")[0],column[5]] for column in self.mycursor]
            string_data_type=['varchar','char']
            int_data_type=['int']
            float_data_type=['decimal']
            datetime_data_type=["timestamp"]
            user_choice_string=""
            for index,column in enumerate(column_list):
                user_choice_string+="\n"+str(index)+" : "+column[0]

            try:
                user_choice=int(input("enter data which you want to update "+user_choice_string+": "))
                if(column_list[user_choice][1] in string_data_type):
                    return(table_name,[column_list[user_choice][0],input("enter {0} condition string only: ".format(column_list[user_choice][0]))])
                elif(column_list[user_choice][1] in int_data_type):
                    return ( table_name,[column_list[user_choice][0],int(input("enter {0} condition int only: ".format(column_list[user_choice][0])))])
                elif(column_list[user_choice][1] in float_data_type):
                    return (table_name,[column[user_choice][0],float(input("enter {0} condition float only: ".format(column_list[user_choice][0])))])
                elif(column_list[user_choice][1] in datetime_data_type):
                    return (table_name,[column_list[user_choice][0],time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S")])
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))
                return "{0} table doesn't exist".format(table_name)

        elif(return_type=="clause_distinct"):
            table_name=input("=======================\nenter table name: ")
            self.mycursor.execute("SHOW COLUMNS FROM "+table_name)
            column_list=[[column[0],str(str(column[1]).split("'")[1]).split("(")[0],column[5]] for column in self.mycursor]
            string_data_type=['varchar','char']
            int_data_type=['int']
            float_data_type=['decimal']
            datetime_data_type=["timestamp"]
            user_choice_string=""
            for index,column in enumerate(column_list):
                user_choice_string+="\n"+str(index)+" : "+column[0]

            try:
                user_choice=int(input("enter data which you want to update "+user_choice_string+": "))
                loggerfile.Logger("info","successfully get records of table {0}".format(table_name))
                return (table_name,column_list[user_choice][0])
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))
                return "{0} table doesn't exist".format(table_name)

        elif(return_type=="clause_form"):
            return input("enter table name: ")

        elif(return_type=="clause_orderby"):
            table_name=input("=======================\nenter table name: ")
            self.mycursor.execute("SHOW COLUMNS FROM "+table_name)
            column_list=[[column[0],str(str(column[1]).split("'")[1]).split("(")[0],column[5]] for column in self.mycursor]
            string_data_type=['varchar','char']
            int_data_type=['int']
            float_data_type=['decimal']
            datetime_data_type=["timestamp"]
            user_choice_string=""
            for index,column in enumerate(column_list):
                user_choice_string+="\n"+str(index)+" : "+column[0]

            try:
                user_choice=int(input("enter condition "+user_choice_string+": "))
                if(column_list[user_choice][1] in string_data_type):
                    condition=[column_list[user_choice][0],input("enter {0} condition string only: ".format(column_list[user_choice][0]))]
                elif(column_list[user_choice][1] in int_data_type):
                    condition=[column_list[user_choice][0],int(input("enter {0} condition int only: ".format(column_list[user_choice][0])))]
                elif(column_list[user_choice][1] in float_data_type):
                    condition=[column[user_choice][0],float(input("enter {0} condition float only: ".format(column_list[user_choice][0])))]
                elif(column_list[user_choice][1] in datetime_data_type):
                    condition=[column_list[user_choice][0],time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S")]
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))


            try:
                user_choice=int(input("enter order by condition "+user_choice_string+": "))
                loggerfile.Logger("info","successfully get records of table {0}".format(table_name))
                column=column_list[user_choice][0]
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))

            return (table_name,condition,column)
    
        elif(return_type=="clause_groupby"):
            table_name=input("=======================\nenter table name: ")
            self.mycursor.execute("SHOW COLUMNS FROM "+table_name)
            column_list=[[column[0],str(str(column[1]).split("'")[1]).split("(")[0],column[5]] for column in self.mycursor]
            user_choice_string=""
            for index,column in enumerate(column_list):
                user_choice_string+="\n"+str(index)+" : "+column[0]

            try:
                user_choice=int(input("enter condition "+user_choice_string+": "))
                loggerfile.Logger("info","successfully get records of table {0}".format(table_name))
                condition=column_list[user_choice][0]
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))

            try:
                user_choice=int(input("enter groupy_by_condition "+user_choice_string+": "))
                loggerfile.Logger("info","successfully get records of table {0}".format(table_name))
                group_by_condition=column_list[user_choice][0]
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))

            return (table_name,condition,group_by_condition)