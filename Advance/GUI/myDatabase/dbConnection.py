import mysql.connector

db = mysql.connector.connect(
    user='root', 
    password='Vivek@2003',  
    host='127.0.0.1',
    database='Vivekdb'
)

cursor = db.cursor()