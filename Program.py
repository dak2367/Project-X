from User import User
import sqlite3
from flask import Flask, jsonify

def main():
    sqlConnection = sqlite3.connect("Database.db")
    sqlCursor = sqlConnection.cursor()

    print("Create")
    print("Sign Up")