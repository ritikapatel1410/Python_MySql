'''
@Author: Ritika Patidar
@Date: 2021-03-15 23:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 23:10:38  
@Title : perform view operation 
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class View_Operation:
    """
        Description:
            this class is define for perform different operation on view
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Create_View(self):
        """
            Description:
                this function is define for create view
            Parameter:
                None
            Return:
                return "View_Customer view created" if view created else "View_Customer view already exist"
        """
        try:
            print("================================ Create View Table ===================================")
            self.mycursor.execute("CREATE VIEW View_Customer AS SELECT NAME, AGE FROM CUSTOMERS")
            result = self.mycursor.fetchall()
            loggerfile.Logger("info","create view successfully")
            return "View_Customer view created"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "View_Customer view already exist"

    def Update_View(self):
        """
            Description:
                this function is define for Update View
            Parameter:
                None
            Return:
                View_Customer updated successfully
        """
        try:
            print("================================ Update View ===================================")
            self.mycursor.execute("ALTER VIEW View_Customer AS SELECT NAME,ADDRESS FROM CUSTOMERS")
            result = self.mycursor.fetchall()
            loggerfile.Logger("info","update view successfully")
            return "View_Customer updated successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Show_View(self):
        """
            Description:
                this function is define for show view
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ Show View ===================================")
            self.mycursor.execute("SELECT * FROM View_Customer")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","show view successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
        
    def Drop_View(self):
        """
            Description:
                this function is define for drop view
            Parameter:
                None
            Return:
                View_Customer deleted successfully
        """
        try:
            print("================================ Drop View ===================================")
            self.mycursor.execute("DROP VIEW IF EXISTS View_Customer")
            result = self.mycursor.fetchall()
            loggerfile.Logger("info","drop view successfully")
            return "View_Customer deleted successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    
   
    