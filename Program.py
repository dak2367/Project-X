from User import User
import sys
import sqlite3

def main():
    sqlConnection = sqlite3.connect("Database.db")
    sqlCursor = sqlConnection.cursor()
    
    print("Hello world")