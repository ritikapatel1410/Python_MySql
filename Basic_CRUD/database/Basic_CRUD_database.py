'''
@Author: Ritika Patidar
@Date: 2021-03-12 17:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-12 17:10:38  
@Title : perform basic curd operation on database
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config
class Basic_CRUD_DB:
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'))
        self.mycursor = self.mydb.cursor()
    def create_db(self,database_name):
        try:
            self.mycursor.execute("CREATE DATABASE IF NOT EXISTS "+ database_name)
            loggerfile.Logger("info","created database {0} successfully".format(database_name))
            return "created database {0} successfully".format(database_name)
        except NameError as error:
            print(error)
            loggerfile.Logger("error","{0} database already exist".format(database_name))
            return "{0} database already exist".format(database_name)
        except Exception as error:
            print(error)
            loggerfile.Logger("error","{0} database already exist".format(database_name))
            return "{0} database already exist".format(database_name)

    def show_list_of_db(self):
        try:
            self.mycursor.execute("SHOW DATABASES")
            print("================================ list of database ===================================")
            for database in self.mycursor:
                print(database) 
            return "successfully get the list of data"
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "not possible"

    def drop_db(self,database_name):
        try:
            self.mycursor.execute("DROP DATABASE "+database_name)
            loggerfile.Logger("info","{0} successfully deleted database".format(database_name))
            return "{0} successfully deleted database".format(database_name)
        except NameError as error:
            loggerfile.Logger("error","{0} database doesn't exist".format(database_name))
            return "{0} database doesn't exist".format(database_name)
        except Exception as error:
            loggerfile.Logger("error","{0} database doesn't exist".format(database_name))
            return "{0} database doesn't exist".format(database_name)
    
        
def input_database():
    return input("enter the database name: ")
