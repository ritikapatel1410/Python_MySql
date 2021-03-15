'''
@Author: Ritika Patidar
@Date: 2021-03-15 17:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 17:10:38  
@Title : perform aggregate function on table
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class Aggregate_Function:
    """
        Description:
            this class is define for show the functionality of Aggregate Function
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Count_Fuction(self):
        """
            Description:
                this function is define for count name of CUSTOMERS table
            Parameter:
                None
            Return:
                return count of name if table exist else count function not performed successfully
        """
        try:
            print("================================ count of name ===================================")
            self.mycursor.execute("SELECT COUNT(name) FROM CUSTOMERS")
            count = self.mycursor.fetchone()
            loggerfile.Logger("info","count  {0} successfully".format( count))
            return "count : {0}".format(count)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "count function not performed successfully"
    def Sum_Fuction(self):
        """
            Description:
                this function is define for sum of salary of CUSTOMERS table
            Parameter:
                None
            Return:
                return sum of salary if table exist else salary function not performed successfully
        """
        try:
            print("================================ sum of salary ===================================")
            self.mycursor.execute("SELECT SUM(SALARY) AS 'Total Salary' FROM CUSTOMERS")
            Sum = self.mycursor.fetchone()
            loggerfile.Logger("info","total salary  {0} get successfully".format(Sum))
            return "total salary : {0}".format(Sum)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "sum function not performed successfully"

    def AVG_Fuction(self):
        """
            Description:
                this function is define for Average of salary of CUSTOMERS table
            Parameter:
                None
            Return:
                return avg of salary if table exist else avg function not performed successfully
        """
        try:
            print("================================ avg salary ===================================")
            self.mycursor.execute("SELECT AVG(SALARY) AS 'AVG Salary' FROM CUSTOMERS")
            AVG=self.mycursor.fetchall()
            loggerfile.Logger("info","average salary  {0} get successfully".format(AVG))
            return "avg salary : {0}".format(AVG)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "avg function not performed successfully"

    def Min_Fuction(self):
        """
            Description:
                this function is define for min of salary of CUSTOMERS table
            Parameter:
                None
            Return:
                return min of salary if table exist else min function not performed successfully
        """
        try:
            print("================================ minmum salary ===================================")
            self.mycursor.execute("SELECT MIN(SALARY) AS 'Minimum Salary' FROM CUSTOMERS")
            Min=self.mycursor.fetchall()
            loggerfile.Logger("info","Min  {0} get successfully".format(Min))
            return "minimum salary : {0}".format(Min)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "min function not performed successfully"

    def Max_Fuction(self):
        """
            Description:
                this function is define for max of salary of CUSTOMERS table
            Parameter:
                None
            Return:
                return max of salary if table exist else max function not performed successfully
        """
        try:
            print("================================ maximum salary ===================================")
            self.mycursor.execute("SELECT MAX(SALARY) AS 'Maximum Salary' FROM CUSTOMERS")
            Max=self.mycursor.fetchall()
            loggerfile.Logger("info","Max  {0} get successfully".format(Max))
            return "maximum salary : {0}".format(Max)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "max function not performed successfully"

    def First_Fuction(self):
        """
            Description:
                this function is define for first entry of name column of CUSTOMERS table
            Parameter:
                None
            Return:
                return first entry of name column if table exist else first function not performed successfully
        """
        try:
            print("================================ First Value ===================================")
            self.mycursor.execute("SELECT name FROM CUSTOMERS LIMIT 1")
            Fist_value=self.mycursor.fetchall()
            loggerfile.Logger("info","First Value  {0} get successfully".format(Fist_value))
            return "first value : {0}".format(Fist_value)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "First function not performed successfully"

    def Last_Fuction(self):
        """
        Description:
            this function is define for last entry of name column of CUSTOMERS table
        Parameter:
            None
        Return:
            return last entry of name column if table exist else first function not performed successfully
        """
        try:
            print("================================ Last Value ===================================")
            self.mycursor.execute("SELECT name FROM CUSTOMERS ORDER BY name DESC LIMIT 1")
            Last_Value=self.mycursor.fetchall()
            loggerfile.Logger("info","Last Value  {0} get successfully".format(Last_Value))
            return "Last Value : {0}".format(Last_Value)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "Last function not performed successfully"