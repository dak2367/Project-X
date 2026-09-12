import sqlite3

class DatabaseManager:
    def __init__(self, databaseName = "Database.db"):
        self.databaseName = databaseName

    # HELPER METHOD FOR CONNECTION
    def createConnection(self):
        return sqlite3.connect(self.databaseName)

    def createTable(self):
        dbConnection = self.createConnection
        cursor = dbConnection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY
                username TEXT
                name TEXT
                email TEXT
                password TEXT
                )
                """
        )
        dbConnection.commit()

    # def addUser(self, username, name, email, password):

