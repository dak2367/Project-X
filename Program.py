from User import User
from DatabaseManager import DatabaseManager
import sqlite3
from flask import Flask, jsonify

def main():
    db = DatabaseManager("Database.db")

    print("Create")
    print("Sign Up")