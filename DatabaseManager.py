import sqlite3

class DatabaseManager:
    def __init__(self, databaseName = "Database.db"):
        self.databaseName = databaseName

    # HELPER METHOD FOR CONNECTION
    def createConnection(self):
        return sqlite3.connect(self.databaseName)
