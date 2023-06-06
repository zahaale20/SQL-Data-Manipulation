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

        # In the table specifying which instruments the band members play on each song (we refer to it as the
        # ”instruments table” below), replace all occurrences of ’bass balalaika’ with ’awesome bass balalaika’, 
        # and all occurrences of ’guitar’ with ’acoustic guitar’. (Please note that you may need to change the length 
        # of the instrument name field if it is not long enough in your table - do it using a table schema modification command, 
        # rather than in the CREATE TABLE statement).
        cursor.execute("ALTER TABLE Instruments MODIFY Instrument VARCHAR(50);")
        cursor.execute("UPDATE Instruments SET Instrument = 'awesome bass balalaika' WHERE Instrument = 'bass balalaika';")
        cursor.execute("UPDATE Instruments SET Instrument = 'acoustic guitar' WHERE Instrument = 'guitar';")

        # Keep in the instruments table only the information about ’awesome bass balalaika’ players and the information about all
        # instruments Anne-Marit (her band member id is 3 - you can use it directly) played on all songs.
        cursor.execute("CREATE TABLE temp AS SELECT * FROM Instruments WHERE Instrument = 'awesome bass balalaika' OR BandmateId = 3;")
        cursor.execute("DROP TABLE Instruments;")
        cursor.execute("RENAME TABLE temp TO Instruments;")

        # Run the following SQL query:
        cursor.execute("SELECT * FROM Instruments ORDER BY SongId, BandmateId;")
        for row in cursor.fetchall():
            print(row)

        # Add a new attribute to the table describing the albums released by Katzenjammer. The attribute should store the total 
        # number of songs on the album.
        cursor.execute("ALTER TABLE Albums ADD NumSongs INT;")

        # Based on information stored in the tracklists table (look up the CSV file if you have to), update each record in the 
        # albums table to show the correct number of tracks.
        cursor.execute("SELECT AlbumId, COUNT(*) FROM Tracklists GROUP BY AlbumId;")
        for row in cursor.fetchall():
            cursor.execute("UPDATE Albums SET NumSongs = %s WHERE AId = %s;", (row[1], row[0]))

        # Run the following SQL query:
        cursor.execute("SELECT * FROM Albums ORDER BY Year;")
        for row in cursor.fetchall():
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


