'''
@Author: Ritika Patidar
@Date: 2021-03-12 17:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-12 17:10:38  
@Title : perform mysql clause on table
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class clause:
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def clause_where(self,table_name,condition):
        try:
            print("================================ Column statisfied where condition ===================================")
            self.mycursor.execute("SELECT * FROM "+table_name+" WHERE "+condition[0]+" = "+"'"+condition[1]+"'")
            for column in self.mycursor:
                print(column) 
            loggerfile.Logger("info","created data from {0} successfully".format(table_name))
            return "successfully get the records of table"
        except NameError as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "{0} table not exist".format(table_name)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "{0} table not exist".format(table_name)

    def clause_distinct(self,table_name,column):
        try:
            self.mycursor.execute("SELECT DISTINCT "+column+" FROM "+table_name)
            print("================================ Distinct Column ===================================")
            for column in self.mycursor:
                print(column) 
            return "successfully get the records of table"
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "not possible"

    def clause_form(self,table_name):
        try:
            self.mycursor.execute("SELECT * FROM "+table_name)
            print("================================ all columns of {0} ===================================".format(table_name))
            for column in self.mycursor:
                print(column) 
            loggerfile.Logger("info","successfully get the records of {0} table".format(table_name))
            return "successfully get the records of {0} table".format(table_name)
        except NameError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)

    def clause_orderby(self,table_name,condition,order_by_condition):
        try:
            self.mycursor.execute("SELECT * FROM "+table_name+" WHERE "+condition[0]+" = "+"'"+condition[1]+"'"+" ORDER BY "+order_by_condition)
            print("================================ all columns of {0} ===================================".format(table_name))
            for column in self.mycursor:
                print(column) 
            loggerfile.Logger("info","successfully get the records of {0} table".format(table_name))
            return "successfully get the records of {0} table".format(table_name)
        except NameError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)

    def clause_groupby(self,table_name,condition,group_by_condition):
        try:
            self.mycursor.execute("SELECT "+condition+", COUNT(*) FROM "+table_name+" GROUP BY "+group_by_condition)
            print("================================ all columns of {0} ===================================".format(table_name))
            for column in self.mycursor:
                print(column) 
            loggerfile.Logger("info","successfully get the records of {0} table".format(table_name))
            return "successfully get the records of {0} table".format(table_name)
        except NameError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
            return "{0} table doesn't exist".format(table_name)

