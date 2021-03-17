'''
@Author: Ritika Patidar
@Date: 2021-03-17 22:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-17 22:10:38  
@Title : perform window aggregate function on table
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
            this class is define for show the functionality of window Aggregate Function
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
            print("================================ count of sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, Count(Sale) OVER(PARTITION BY Year) AS Total_Sales FROM Sales")
            count = self.mycursor.fetchall()
            for records in count:
                print(records)
            loggerfile.Logger("info","count  {0} successfully".format( count))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

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
            print("================================ sum of Sale===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, SUM(Sale) OVER(PARTITION BY Year) AS Total_Sales FROM Sales")
            Sum = self.mycursor.fetchall()
            for records in Sum:
                print(records)
            loggerfile.Logger("info","total salary  {0} get successfully".format(Sum))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def AVG_Fuction(self):
        """
            Description:
                this function is define for Average of sale of CUSTOMERS table
            Parameter:
                None
            Return:
                return avg of salary if table exist else avg function not performed successfully
        """
        try:
            print("================================ avg sale===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, AVG(Sale) OVER(PARTITION BY Year) AS Total_Sales FROM Sales")
            AVG=self.mycursor.fetchall()
            for records in AVG:
                print(records)
            loggerfile.Logger("info","average salary  {0} get successfully".format(AVG))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

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
            print("================================ minimum sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, MIN(Sale) OVER(ORDER BY year) AS Total_Sales FROM Sales")
            Min=self.mycursor.fetchall()
            for records in Min:
                print(records)
            loggerfile.Logger("info","Min  {0} get successfully".format(Min))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


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
            print("================================ maximum sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, Max(Sale) OVER(PARTITION BY Year) AS Total_Sales FROM Sales")
            Max=self.mycursor.fetchall()
            for records in Max:
                print(records)
            loggerfile.Logger("info","Max  {0} get successfully".format(Max))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


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
            self.mycursor.execute("SELECT Year, Product, Sale, MIN(Sale) OVER(ORDER BY Product) AS Total_Sales FROM Sales LIMIT 1")
            Fist_value=self.mycursor.fetchone()
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
            self.mycursor.execute("SELECT Year, Product, Sale, MIN(Sale) OVER(ORDER BY Product DESC) AS Total_Sales FROM Sales LIMIT 1")
            Last_Value=self.mycursor.fetchall()
            loggerfile.Logger("info","Last Value  {0} get successfully".format(Last_Value))
            return "Last Value : {0}".format(Last_Value)
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
            return "Last function not performed successfully"