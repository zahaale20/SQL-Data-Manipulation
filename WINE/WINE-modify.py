# Alex Zaharia
# azaharia@calpoly.edu
# May 2, 2023

import mysql.connector
from mysql.connector import Error

pwdfileName = 'account.info'
with open(pwdfileName, 'r') as pwdfile:
    lines = pwdfile.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

hostName = 'mysql.labthreesixfive.com'
portName = '3306'
userName = username
passString = password

dbName = 'azaharia'


try:

    conn = mysql.connector.connect(host=hostName, port=portName, database=dbName,
                                   user=userName, password=passString)
    if conn.is_connected():
        print('Connected to', hostName)

        cursor = conn.cursor()

        # Remove the columns storing the appelation name and the name of the wine from the table storing the 
        # list of wines (we refer to this table as ”the wine table”)
        cursor.execute("ALTER TABLE wine DROP COLUMN Appellation, DROP COLUMN WName")

        # Keep in the wine table only the Zinfandels with a score of 92 or higher.
        cursor.execute("DELETE FROM wine WHERE Grape='Zinfandel' AND Score<92")

        # Add a new column to the table called Revenue. It should have the same type as your price column.
        cursor.execute("ALTER TABLE wine ADD COLUMN Revenue INTEGER")

        # A case is 12 bottles of wine. Using the information available to you, set the revenue for each wine 
        # left in the table to be equal to the total amount of money that can be made by selling all the cases of the wine.
        cursor.execute("UPDATE wine SET Revenue = Price * Cases / 12")

        # Output the list of wines using the following SQL query:
        cursor.execute("SELECT * FROM wine ORDER BY Revenue")
        wines = cursor.fetchall()
        for wine in wines:
            print(wine)

        # Close the cursor and connection
        conn.commit()
        cursor.close()



except Error as e:
    print('Connection error: ', e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('Done')


