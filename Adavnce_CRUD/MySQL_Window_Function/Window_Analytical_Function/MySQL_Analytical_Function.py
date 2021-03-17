'''
@Author: Ritika Patidar
@Date: 2021-03-18 00:30:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-18 00:30:38  
@Title : perform window analytical function on table
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class Analytical_Function:
    """
        Description:
            this class is define for show the functionality of Window Analytical Function
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def NTILE_Function(self):
        """
            Description:
                this function is define for Ntile Function
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ NTILE Function ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale,NTile(4) OVER() AS Total_Sales FROM Sales")
            ntile = self.mycursor.fetchall()
            for records in ntile:
                print(records)
            loggerfile.Logger("info","ntile fuction performed successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    def LEAD_Function(self):
        """
            Description:
                this function is define for LEAD function
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ LEAD Function ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale,LEAD(Sale,1) OVER(ORDER BY Year) AS Total_Sales FROM Sales")
            lead = self.mycursor.fetchall()
            for records in lead:
                print(records)
            loggerfile.Logger("info","lead functions performed successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def LAG_Function(self):
        """
            Description:
                this function is define for Lag Function
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ Lag Function ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale,LAG(Sale,2) OVER(ORDER BY Year) AS Total_Sales FROM Sales")
            percentage_rank=self.mycursor.fetchall()
            for records in percentage_rank:
                print(records)
            loggerfile.Logger("info","Leg fuctions performed successfully".format(AVG))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    def FIRST_VALUE_Function(self):
        """
            Description:
                this function is define for FIRST_VALUE Function
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ First Value Function ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, FIRST_VALUE(Product) OVER(PARTITION BY Year order by Sale desc) AS Total_Sales FROM Sales")
            first_value=self.mycursor.fetchall()
            for records in first_value:
                print(records)
            loggerfile.Logger("info","First value function performed successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def  LAST_VALUE_Function(self):
        """
            Description:
                this function is define for LAST_VALUE Function
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ Last Value Function ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale,  LAST_VALUE(Product) OVER(PARTITION BY Year order by Sale desc) AS Dume_Dist_Sale FROM Sales")
            last_value=self.mycursor.fetchall()
            for records in last_value:
                print(records)
            loggerfile.Logger("info","Last value performed successfully".format(Max))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

