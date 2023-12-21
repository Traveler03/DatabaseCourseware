import pyodbc

class Database:
    def __init__(self, server, database, username, password):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                         server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    def get_connection(self):
        return self.connection
