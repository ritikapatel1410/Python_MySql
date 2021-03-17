'''
@Author: Ritika Patidar
@Date: 2021-03-12 13:50:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-12 13:50:38  
@Title : code for input of perform basic curd operation on table
'''
import mysql.connector as mysql 
from decouple import config
import time
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile

class Input_CRUD:
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
        self.commit=self.mydb.commit()

    def input_function(self,return_type):
        if(return_type=="create_table" or return_type=="show_records"):
            return input("enter table name: ")
        elif(return_type=="insert_data"):
            try:
                table_name=input("enter table name: ")
                self.mycursor.execute("SHOW COLUMNS FROM "+table_name)
                column_list=[[column[0],str(str(column[1]).split("'")[1]).split("(")[0],column[5]] for column in self.mycursor]
                string_data_type=['varchar','char']
                int_data_type=['int']
                float_data_type=['decimal']
                datetime_data_type=["timestamp"]
                insert_value=[]
                insert_column_name=[]
                for column in column_list:
                    if(column[2]!="auto_increment"):
                        if(column[1] in string_data_type):
                            insert_value.append(input("enter {0} value: ".format(column[0])))
                            insert_column_name.append(column[0])
                        elif(column[1] in int_data_type):
                            insert_value.append(int(input("enter {0} value :".format(column[0]))))
                            insert_column_name.append(column[0])
                        elif(column[1] in float_data_type):
                            insert_value.append(float(input("enter {0} value :".format(column[0]))))
                            insert_column_name.append(column[0])
                        elif(column[1] in datetime_data_type):
                            insert_value.append(time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S"))
                            insert_column_name.append(column[0])

                return (table_name,tuple(insert_value),insert_column_name)
            except Exception as error:
                return "{0}".format(error)

        elif(return_type=="delete_records"):
            table_name=input("enter table name: ")
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
                user_choice=int(input("enter data which you want to delete "+user_choice_string+": "))
                if(column_list[user_choice][1] in string_data_type):
                    return (table_name,column_list[user_choice][0],input("enter {0} update value string only: ".format(column_list[user_choice][0])))
                elif(column_list[user_choice][1] in int_data_type):
                    return (table_name,column_list[user_choice][0],int(input("enter {0} update value int only: ".format(column_list[user_choice][0]))))
                elif(column_list[user_choice][1] in float_data_type):
                    return (table_name,column_list[user_choice][0],float(input("enter {0} update value float only: ".format(column_list[user_choice][0]))))
                elif(column_list[user_choice][1] in datetime_data_type):
                    return (table_name,column_list[user_choice][0],time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S"))
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))

        elif(return_type=="add_column_table"):
            table_name=input("enter table name: ")
            column_name=input("enter column name: ")
            try:
                select_dtype=int(input("=================== select data type =========================\nint : 0\nfloat : 1\nstring : 2\ndatetime : 3\nenter : "))
                if(select_dtype==0):
                    return (table_name,column_name,"INT")
                elif(select_dtype==1):
                    return (table_name,column_name,"DECIMAL")
                elif(select_dtype==2):
                    return (table_name,column_name,"VARCHAR")
                elif(select_dtype==3):
                    return (table_name,column_name,"TIMESTAMP")
            except Exception as error :
                loggerfile.Logger("error","{0} occured".format(error))

        elif(return_type=="update_data"):
            table_name=input("enter table name: ")
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
                    update_data=[column_list[user_choice][0],input("enter {0} condition string only: ".format(column_list[user_choice][0]))]
                elif(column_list[user_choice][1] in int_data_type):
                    update_data=[column_list[user_choice][0],int(input("enter {0} condition int only: ".format(column_list[user_choice][0])))]
                elif(column_list[user_choice][1] in float_data_type):
                    update_data=[column[user_choice][0],float(input("enter {0} condition float only: ".format(column_list[user_choice][0])))]
                elif(column_list[user_choice][1] in datetime_data_type):
                    update_data=[column_list[user_choice][0],time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S")]
                
                user_choice_condition=int(input("enter condition "+user_choice_string+": "))
                if(column_list[user_choice_condition][1] in string_data_type):
                    condition=[column_list[user_choice_condition][0],input("enter {0} condition string only: ".format(column_list[user_choice_condition][0]))]
                elif(column_list[user_choice_condition][1] in int_data_type):
                    condition=[column_list[user_choice_condition][0],int(input("enter {0} condition int only: ".format(column_list[user_choice_condition][0])))]
                elif(column_list[user_choice_condition][1] in float_data_type):
                    condition=[column_list[user_choice][0],float(input("enter {0} condition float only: ".format(column_list[user_choice_condition][0])))]
                elif(column_list[user_choice_condition][1] in datetime_data_type):
                    condition=[column_list[user_choice][0],time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S")]

                return (table_name,update_data,condition)
            except Exception as error:
                loggerfile.Logger("error","{0} occured".format(error))