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

        # Keep in the table storing the technical characteristics about the cars (we refer to this table as ”the cardata
        #  table”), ONLY the records that satisfy at least one of the following conditions: (a) vehicles made in 1978 or 1979 with
        #  MPG of 20 or above. (b) vehicles that have MPG of 26 miles per gallon or better what have an engine with more than 110
        #  horsepowers. (c) vehicles that have 8 cylinders and accelerate to 60 mph in less than 10 seconds.

        cursor.execute("DELETE FROM CarsData WHERE (Year = 1978 OR Year = 1979) AND MPG < 20;")

        cursor.execute("DELETE FROM CarsData WHERE MPG >= 26 AND Horsepower <= 110;")

        cursor.execute("DELETE FROM CarsData WHERE Cylinders = 8 AND Accelerate >= 10;")

        # Order the table by year and car ID
        cursor.execute("SELECT * FROM CarsData ORDER BY Year, Id;")
        for row in cursor:
            print(row)

        # Remove all attributes except car id, car year, acceleration, MPG, and number of cylinders
        cursor.execute("ALTER TABLE CarsData DROP COLUMN Edispl, DROP COLUMN Horsepower, DROP COLUMN Weight;")

        # Remove information about all cars with 5 cylinders or fewer
        cursor.execute("DELETE FROM CarsData WHERE Cylinders <= 5;")

        # Order the table by year and car ID
        cursor.execute("SELECT * FROM CarsData ORDER BY Year, Id;")
        for row in cursor:
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


