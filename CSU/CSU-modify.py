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

        # Keep in the table documenting campus enrollments by discipline only the information about the following enrollments:
        # Engineering majors from Cal Poly San Luis Obispo, Cal Poly Pomona, and Humboldt State University.
        # San Jose State enrollements for disciplines with more than 500 graduate students.
        # All enrollments in LA County CSUs where graduate enrollment exceeds undergraduate enrollment for the same discipline.
        cursor.execute("""
            DELETE FROM DisciplineEnrollments WHERE 
            (CampusId NOT IN (SELECT Id FROM Campuses WHERE Campus IN ('Cal Poly San Luis Obispo', 'Cal Poly Pomona', 'Humboldt State University')))
            OR
            (CampusId = (SELECT Id FROM Campuses WHERE Campus = 'San Jose State') AND GradEnrollment <= 500)
            OR
            (CampusId IN (SELECT Id FROM Campuses WHERE County = 'Los Angeles') AND GradEnrollment <= UndergradEnrollment)
        """)

        # Output the remaining contents of the discipline enrollments table using the following SQL statement:
        cursor.execute("""
            SELECT * FROM DisciplineEnrollments
            ORDER BY CampusId, DisciplineId
        """)
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Keep in the table documenting CSU fees only the information that matches ALL the conditions below:
        # The fee is greater than $2.500;
        # The year is either 2002 or one of 2004—2006.
        # The campus is either Cal Poly San Luis Obispo, Cal Poly Pomona or San Diego State.
        cursor.execute("""
            DELETE FROM CSUFees WHERE 
            CampusFee <= 2500 
            OR 
            (Year NOT IN (2002, 2004, 2005, 2006))
            OR
            (Campus NOT IN (20, 14, 17))
        """)

        # Output the remaining contents of the fees table using the following SQL command:
        cursor.execute("""
            SELECT * FROM CSUFees
            ORDER BY Campus, Year
        """)
        results = cursor.fetchall()
        for row in results:
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


