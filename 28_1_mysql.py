import MySQLdb
import mysql.connector

def main():
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    print(db_connection)
    

if __name__=="__main__":
    main()
