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

        # Remove pastries that are cheaper than $5
        cursor.execute("DELETE FROM items WHERE Item IN (SELECT Id FROM goods WHERE Price < 5)")
        cursor.execute("DELETE FROM goods WHERE Price < 5")

        # Increase the prices of chocolate-flavored items by 35%
        cursor.execute("UPDATE goods SET Price = Price * 1.35 WHERE Flavor = 'chocolate'")

        # Reduce the prices of lemon-flavored items by $2
        cursor.execute("UPDATE goods SET Price = Price - 2 WHERE Flavor = 'lemon'")

        # Reduce the price of all other cakes by 10%
        cursor.execute("UPDATE goods SET Price = Price * 0.9 WHERE Food = 'cake' AND Flavor NOT IN ('lemon', 'chocolate')")

        # Set the price of pie items equal to the price of the least expensive cake
        cursor.execute("SELECT MIN(Price) FROM goods WHERE Food = 'cake'")
        result = cursor.fetchone()
        least_expensive_cake_price = result[0]
        update = "UPDATE goods SET Price = {} WHERE Food = 'pie'".format(least_expensive_cake_price)
        cursor.execute(update)

        # Show the contents of the table
        cursor.execute("SELECT * FROM goods ORDER BY Id")
        result = cursor.fetchall()
        for row in result:
            print(row)
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


