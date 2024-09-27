from .dbConnection import cursor

def create_database():
    database_name = input("Enter a databse name: ")
    QuerySet = f"create database {database_name}"
    cursor.execute(QuerySet)