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

        # Remove from the flights database all flights except for those to and from AKI (that’s the airport code).
        cursor.execute("DELETE FROM flights WHERE SourceAirport != 'AKI' AND DestAirport != 'AKI'")

        # You will be modeling corporate takeover by Continental of all flights except those operated by Virgin and AirTran
        # to and from AKI. For this problem (and this problem ONLY)2, you will look up the numeric IDs for each airline, and 
        # substitute them for airline names in the commands you need to develop.
        cursor.execute("UPDATE flights SET Airline = 7 WHERE Airline = 'Continental Airlines'")
        cursor.execute("UPDATE flights SET Airline = 12 WHERE Airline = 'Virgin America'")
        cursor.execute("UPDATE flights SET Airline = 10 WHERE Airline = 'AirTran Airways'")

        # For all flights NOT operated by Continental, AirTran or Virgin, increase the flight number by 2000 (this will ensure that after
        # the corporate takeover, flight numbers are still unique).
        cursor.execute("UPDATE flights SET FlightNo = FlightNo + 2000 WHERE Airline NOT IN (7, 12, 10)")

        # First, some context on how the data in the Flights table is organized. All flights in this table come in pairs. 
        # The first flight starts at Airport 1 and goes to Airport 2. The second flight goes from Airport 2 to Airport 1 
        # (the return flight). The flight numbers of these two flights are different by 1 - one flight number is even, one is odd. For all 
        # pairs of flights to/from AKI NOT operated by Continental, AirTran, or Virgin, 
        # you need to flip the flight numbers. That is, if a flight from AKI to some other airport had an even flight number N , 
        # it needs to be replaced by N + 1, while, the flight number for a return flight will change from N + 1 to N . 
        # Conversely, if a flight from AKI has an odd flight number N , it needs to be replaced by N − 1, while the flight 
        # number of the return flight needs to change from N − 1 to N .(In other words, all even-numbered flights need to 
        # increase by 1, all odd-numbered flights need to decrease by 1.)
        cursor.execute("UPDATE flights SET FlightNo = FlightNo + MOD(FlightNo, 2)*2 - 1 WHERE Airline NOT IN (7, 12, 10) AND SourceAirport = 'AKI'")
        cursor.execute("UPDATE flights SET FlightNo = FlightNo - MOD(FlightNo, 2)*2 + 2 WHERE Airline NOT IN (7, 12, 10) AND DestAirport = 'AKI'")

        # Complete the corporate takeover. Replace the airline for all flights to and from AKI except for AirTran and Virgin with Continental.
        cursor.execute("UPDATE flights SET Airline = 1 WHERE (SourceAirport = 'AKI' OR DestAirport = 'AKI') AND Airline NOT IN (12, 10)")

        # Output flights table
        cursor.execute("SELECT * FROM flights ORDER BY Airline, FlightNo")
        rows = cursor.fetchall()
        for row in rows:
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


