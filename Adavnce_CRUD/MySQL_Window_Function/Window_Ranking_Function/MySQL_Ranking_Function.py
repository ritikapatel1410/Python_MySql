'''
@Author: Ritika Patidar
@Date: 2021-03-17 23:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-17 23:10:38  
@Title : perform window ranking function on table
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class Ranking_Function:
    """
        Description:
            this class is define for show the functionality of window Ranking Function
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def RANK_Fuction(self):
        """
            Description:
                this function is define for RANK sale of sales table
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ RANK of sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, RANK() OVER(PARTITION BY product order by Sale desc) AS Rank_Sale FROM Sales")
            rank = self.mycursor.fetchall()
            for records in rank:
                print(records)
            loggerfile.Logger("info","RANK Function successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    def DENSE_RANK_Fuction(self):
        """
            Description:
                this function is define for DENSE_RANK sale of sales table
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ sum of Sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, DENSE_RANK() OVER(PARTITION BY product order by Sale desc) AS Dense_Rank_Sale FROM Sales")
            dense_rank = self.mycursor.fetchall()
            for records in dense_rank:
                print(records)
            loggerfile.Logger("info","DENSE_RANK function performed successfully uccessfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def PERCENT_RANK_Fuction(self):
        """
            Description:
                this function is define for PERCENT_RANK of sale of sales table
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ PERCENT_RANK sale===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, PERCENT_RANK() OVER(PARTITION BY product order by Sale desc) AS Percent_Rank_sale FROM Sales")
            percentage_rank=self.mycursor.fetchall()
            for records in percentage_rank:
                print(records)
            loggerfile.Logger("info","PERCENT_RANK function performed successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    def ROW_NUMBER_Fuction(self):
        """
            Description:
                this function is define for ROW_NUMBER sale of sales table
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ ROW_NUMBER sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale, ROW_NUMBER() OVER(PARTITION BY product order by Sale desc) AS Row_Number_sale FROM Sales")
            row_number=self.mycursor.fetchall()
            for records in row_number:
                print(records)
            loggerfile.Logger("info","ROW_NUMBER fuction performed get successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def  CUME_DIST(self):
        """
            Description:
                this function is define for CUME_DIST of Sale of Sales table
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ CUME_DIST sale ===================================")
            self.mycursor.execute("SELECT Year, Product, Sale,  CUME_DIST() OVER(PARTITION BY product order by Sale desc) AS Dume_Dist_Sale FROM Sales")
            cume_dist=self.mycursor.fetchall()
            for records in cume_dist:
                print(records)
            loggerfile.Logger("info","CUME_DIST  {0} get successfully".format(Max))
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

