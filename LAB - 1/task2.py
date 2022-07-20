from colorama import Cursor
from mysql.connector import Error
import mysql.connector as msql
import pandas as pd
data = pd.read_csv("CricketDataCSV.csv", index_col=False, delimiter=",")
print(data.head())

try:
    conn = msql.connect(host='localhost', user='root',
                        database='BDA_LAB_1', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE cricket_data (
                Id INT PRIMARY KEY,
                Name VARCHAR(50),
                Fifty INT,
                Century INT
            )
        ''')

        for i, row in data.iterrows():
            query = "INSERT INTO cricket_data VALUES (%s, %s, %s, %s)"
            cursor.execute(query, tuple(row))
            print("Record inserted!!")
            conn.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
