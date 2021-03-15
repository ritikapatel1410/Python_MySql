'''
@Author: Ritika Patidar
@Date: 2021-03-15 00:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 00:10:38  
@Title : perform index operation 
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class Index_Operation:
    """
        Description:
            this class is define for perform different operation of index
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Create_Index(self):
        """
            Description:
                this function is define for create index
            Parameter:
                None
            Return:
                index created"
        """
        try:
            print("================================ Create Index ===================================")
            self.mycursor.execute("CREATE INDEX index_CUSTOMERS ON CUSTOMER_DATA (NAME,AGE)")
            loggerfile.Logger("info","create index successfully")
            return "Index Created"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Explain_Index(self):
        """
            Description:
                this function is define for Explain Index
            Parameter:
                None
            Return:
                "Explained Index successfully"
        """
        try:
            print("================================ Explain Index ===================================")
            self.mycursor.execute("EXPLAIN SELECT NAME, AGE, ADDRESS FROM CUSTOMER_DATA WHERE AGE >= 23")
            result = self.mycursor.fetchall()
            for record in result:
                print(record)
            loggerfile.Logger("info","explain index successfully")
            return "Explained Index successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Show_Index(self):
        """
            Description:
                this function is define for show index
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ Show Index ===================================")
            self.mycursor.execute("SHOW INDEXES FROM CUSTOMER_DATA")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","show index successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
        
    def Drop_Index(self):
        """
            Description:
                this function is define for drop index
            Parameter:
                None
            Return:
                index deleted successfully
        """
        try:
            print("================================ Drop View ===============MySQL_Index/====================")
            self.mycursor.execute("DROP INDEX index_CUSTOMERS ON CUSTOMER_DATA")
            loggerfile.Logger("info","drop index successfully")
            return "index deleted successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    
   
    