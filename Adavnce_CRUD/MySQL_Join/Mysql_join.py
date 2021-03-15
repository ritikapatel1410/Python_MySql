'''
@Author: Ritika Patidar
@Date: 2021-03-15 20:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 20:10:38  
@Title : perform join operation on tables
'''
import mysql.connector as mysql
import os
import sys
sys.path.insert(0,os.path.realpath("LogFile"))
import loggerfile
from decouple import config

class JOIN:
    """
        Description:
            this class is define for different type of join
    """
    def __init__(self):
        self.mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        self.mycursor = self.mydb.cursor()
    def Inner_Join(self):
        """
            Description:
                this function is define for inner join
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ join tables by inner join ===================================")
            self.mycursor.execute("SELECT users.name AS user, products.name AS favorite FROM users INNER JOIN products ON users.fav = products.id")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","table users and products join by inner join successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    def Left_Join(self):
        """
            Description:
                this function is define for left join
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ join tables by left join ===================================")
            self.mycursor.execute("SELECT users.name AS user, products.name AS favorite FROM users RIGHT JOIN products ON users.fav = products.id")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","table users and products join by left join successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))


    def Right_Join(self):
        """
            Description:
                this function is define for Right join
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ join tables by right join  ===================================")
            self.mycursor.execute("SELECT users.name AS user, products.name AS favorite FROM users LEFT JOIN products ON users.fav = products.id")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","table users and products join by right join successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))
        
    def Full_Join(self):
        """
            Description:
                this function is define for Fulln
            Parameter:
                None
            Return:
                None
        """
        try:
            print("================================ join tables by full join ===================================")
            self.mycursor.execute("SELECT users.name AS user, products.name AS favorite FROM users LEFT JOIN products ON users.fav = products.id UNION SELECT users.name AS user, products.name AS favorite FROM users RIGHT JOIN products ON users.fav = products.id")
            result = self.mycursor.fetchall()
            for records in result:
                print(records)
            loggerfile.Logger("info","table users and products join by full join successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} occured".format(error))

    
   
    