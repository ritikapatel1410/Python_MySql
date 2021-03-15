'''
@Author: Ritika Patidar
@Date: 2021-03-16 01:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-16 01:10:38  
@Title : perform store procedure operation 
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class Procedure_Operation:
    """
        Description:
            this class is define for perform different operation on store procedure
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Create_Procedure(self):
        """
            Description:
                this function is define for create store procedure
            Parameter:
                None
            Return:
                return "Procedure created" if view created else "Procedure already exist"
        """
        try:
            print("================================ Create Procedure ===================================")
            self.mycursor.execute("CREATE PROCEDURE get_customer (IN var1 INT) BEGIN SELECT * FROM CUSTOMERS WHERE AGE >=23; SELECT COUNT(Name) AS Total_Customer FROM CUSTOMERS; END;")
 
            loggerfile.Logger("info","create view successfully")
            return "get_customer proceure created"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "get_customer already exist"

    def Show_Procedure(self):
        """
            Description:
                this function is define for show Procedure
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ Show Procedure ===================================")
            self.mycursor.execute("CALL get_customer(3)")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","show Procedure successfully")
            return "show Procedure successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Status_Procedure(self):
        """
            Description:
                this function is define for status of procedure
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ status of procedure ===================================")
            self.mycursor.execute("SHOW PROCEDURE STATUS WHERE db = 'store_data';")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","get status successfully successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
        
    def Drop_Procedure(self):
        """
            Description:
                this function is define for drop Procedure
            Parameter:
                None
            Return:
                get_customer deleted successfully
        """
        try:
            print("================================ Drop View ===================================")
            self.mycursor.execute("DROP PROCEDURE IF EXISTS get_customer")
            result = self.mycursor.fetchall()
            loggerfile.Logger("info","drop get_customer successfully")
            return "get_customer deleted successfully"
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    
   
    