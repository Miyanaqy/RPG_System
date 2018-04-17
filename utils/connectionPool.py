import sqlite3

class ConnectionPool():

    def __init__(self):
        self.connection = []
        while len(self.connection) < 10:
            self.connection.append(sqlite3.connect('RPG_System.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False))

    def getConnection(self):
        if len(self.connection) > 0:
            return self.connection.pop()
        else:
            return sqlite3.connect('RPG_System.db', isolation_level="IMMEDIATE", timeout=60, check_same_thread=False)

    def reConnection(self, connection):
        self.connection.append(connection)
        if len(self.connection) > 10:
            close(self.connection.pop())
    
    def close(self, connection):
        connection.close()
