"""
@Author: Ritika Patidar
@Date: 2021-03-15 16:10:10
@Last Modified by: Ritika Patidar
@Last Modified time: 2021-03-15 16:10:38  
@Title : insert BLOB into mysql
"""


import sys
import os
sys.path.insert(0,os.path.relpath("LogFile"))
import loggerfile
import mysql.connector as mysql
from decouple import config

def convertToBinaryData(filename):
    """
    Description:
        this function is define for convert file into Binary Data
    Parameter:
        None
    Return:
        None
    """
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(name, photo):
    """
    Description:
        this function is define for insert blob into table
    Parameter:
        None
    Return:
        "successfully insert data into student_details"
    """
    try:
        mydb=mysql.connect(host=config('DB_HOST'),user=config('DB_USERNAME'),password=config('DB_PASSWORD'),database=config('DB_DATABASE'))
        mycursor = mydb.cursor()
        sql_insert_blob_query = """ INSERT INTO student_details (student_name, photo) VALUES (%s,%s)"""
        empPicture = convertToBinaryData(photo)
        insert_blob_tuple = (name, empPicture)
        result = mycursor.execute(sql_insert_blob_query, insert_blob_tuple)
        mydb.commit()
        loggerfile.Logger("info","succesfully inset data into student_details")
        return "successfully insert data into student_details"
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

insertBLOB("Vijay", "Image/student1.png")

    
