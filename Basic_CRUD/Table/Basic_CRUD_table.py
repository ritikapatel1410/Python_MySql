'''
@Author: Ritika Patidar
@Date: 2021-03-12 17:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-12 17:10:38  
@Title : perform basic curd operation on table
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config
import time

class Basic_CRUD:
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def create_table(self,table_name):
        Flag=0
        try:
            self.mycursor.execute("CREATE TABLE " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY,datetime TIMESTAMP NOT NULL,name VARCHAR(255), age VARCHAR(255))")
            Flag=1
            loggerfile.Logger("info","{0} successfully created table into database".format(mydb.database))
        except NameError as error:
            Flag=0
            loggerfile.Logger("error","{0} already exist into database".format(mydb.database))
        except Exception as error:
            Flag=0
            loggerfile.Logger("error","{0} already exist into database".format(mydb.database))
        if Flag==1:
            return "table successfully created into {0} database".format(mydb.database)
        else:
            return "table student already exist into {0} database".format(mydb.database)

    def insert_data(self,table_name,val,field_names):
        Flag=0
        no_of_columns=",".join(["%s" for field_name in field_names])
        try:
            datetimeWrite = (time.strftime("%Y-%m-%d ")+time.strftime("%H:%M:%S"))
            sql = "INSERT INTO " + table_name + " "+"("+",".join(field_names)+")"+" VALUES "+"("+no_of_columns+")"
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            Flag=1
            loggerfile.Logger("info","{0}, record inserted".format(self.mycursor.rowcount))
        except Exception as error:
            Flag=0
            loggerfile.Logger("error","{0} error occured".format(error))
        if Flag==1:
            return "insert data successfully"
        else:
            return "not possible"

    def show_records(self,table_name):
        try:
            self.mycursor.execute("SELECT * FROM "+table_name)
            records = self.mycursor.fetchall()
            for record in records:
                print(record) 
            loggerfile.Logger("info","successfully fatched data")
        except Exception as error:
            Flag=0
            loggerfile.Logger("error","{0} error occured".format(error))

    def delete_records(self,table_name,column,column_value):
        Flag=0
        try:
            self.mycursor.execute('DELETE FROM ' +table_name+' WHERE '+column+" = "+'"'+str(column_value)+'"')
            self.mydb.commit()
            Flag=1
            loggerfile.Logger("info","successfully deleted data")
        except Exception as error:
            Flag=0
            loggerfile.Logger("error","{0} error occured".format(error))
        if(Flag==1):
            return "{0} record(s) deleted".format(self.mycursor.rowcount)
        else:
            return "record not exist"

    def add_column_table(self,table_name,column_name,dtype):
        Flag=0
        try:
            print("ALTER TABLE "+table_name+" ADD COLUMN "+column_name+" "+dtype+"(20)")
            self.mycursor.execute("ALTER TABLE "+table_name+" ADD COLUMN "+column_name+" "+dtype+"(20)")
            Flag=1
            loggerfile.Logger("info","successfully added column into student table")
        except NameError as error:
            Flag=0
            loggerfile.Logger("error","{0} occured".format(error))
        except Exception as error:
            Flag=0
            loggerfile.Logger("error","{0} occured".format(error))
        if Flag==1:
            return "successfully added column into student table"
        else:
            return "already exist into column into student table"
        
    def update_data(self,table_name,update_data,update_condition):
        Flag=0
        try:
            sql = "UPDATE "+table_name+" SET "+update_data[0]+" = "+"'"+str(update_data[1])+"'"+" WHERE "+update_condition[0]+" = "+"'"+str(update_condition[1])+"'"
            self.mycursor.execute(sql)
            self.mydb.commit()
            Flag=1
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            Flag=0
        if(Flag==1):
            return "{0} record(s) affected".format(self.mycursor.rowcount,)
        else:
            return "not possible"
