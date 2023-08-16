import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sar99jim99!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE deh")