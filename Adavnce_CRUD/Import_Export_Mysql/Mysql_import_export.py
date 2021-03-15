'''
@Author: Ritika Patidar
@Date: 2021-03-15 02:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 02:10:38  
@Title : perform import export operation
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config
import csv
import xlwt
import pandas.io.sql as sql

class Import_Export:
    """
        Description:
            this class is define for perform import export operation
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Export_table_csv(self):
        """
            Description:
                this function is define for Export table in csv format
            Parameter:
                None
            Return:
                export data successfully
        """
        try:
            self.mycursor.execute("SELECT * FROM CUSTOMERS")
            with open('File/outfile.csv','w') as f:
                writer = csv.writer(f)
                for row in self.mycursor.fetchall():
                    writer.writerow(row)
            loggerfile.Logger("info","export table in csv format successfully")
            return "export data successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Export_table_excel(self):
        """
            Description:
                this function is define for Export table in xls for format
            Parameter:
                None
            Return:
                export data successfully
        """
        try:
            df=sql.read_sql("SELECT * FROM CUSTOMERS",self.mydb)
            df.to_excel('File/ds.xls')
            loggerfile.Logger("info","export table in excel format successfully")
            return "export data successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Import_Table_csv(self):
        """
            Description:
                this function is define for import table from csv file 
            Parameter:
                None
            Return:
                None
        """
        try:
            csv_data = csv.reader(open('File/import_data.csv'))
            next(csv_data)
            for row in csv_data:
                self.mycursor.execute('INSERT INTO CUSTOMER_CSV(name, age,address,salary)VALUES(%s, %s, %s, %s)',row[1:])
            self.mydb.commit()
            loggerfile.Logger("info","import table from csv file successfully")
            return "succesfully import table "
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    
   
    