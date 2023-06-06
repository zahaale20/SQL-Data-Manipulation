-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE Rooms (
  RoomId VARCHAR(3) PRIMARY KEY,
  roomName VARCHAR(255) NOT NULL,
  beds INTEGER NOT NULL,
  bedType VARCHAR(255) NOT NULL,
  maxOccupancy INTEGER NOT NULL,
  basePrice DECIMAL(10, 2) NOT NULL,
  decor VARCHAR(255) NOT NULL
) DEFAULT CHARSET=utf8;

CREATE TABLE Reservations (
  Code INT PRIMARY KEY,
  Room VARCHAR(3) NOT NULL,
  CheckIn DATE NOT NULL,
  CheckOut DATE NOT NULL,
  Rate DECIMAL(10, 2) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  FirstName VARCHAR(255) NOT NULL,
  Adults INTEGER NOT NULL,
  Kids INTEGER NOT NULL,
  CONSTRAINT uc_Reservations_Room_CheckIn_CheckOut UNIQUE (Room, CheckIn, CheckOut),
  FOREIGN KEY (Room) REFERENCES Rooms(RoomId)
) DEFAULT CHARSET=utf8;

ALTER TABLE Reservations MODIFY COLUMN CheckIn DATE NOT NULL DEFAULT '0000-00-00';
ALTER TABLE Reservations MODIFY COLUMN CheckOut DATE NOT NULL DEFAULT '0000-00-00';

SET sql_mode = '';
ALTER TABLE Reservations MODIFY COLUMN CheckIn VARCHAR(15) NOT NULL DEFAULT '';
ALTER TABLE Reservations MODIFY COLUMN CheckOut VARCHAR(15) NOT NULL DEFAULT '';

UPDATE Reservations SET CheckIn = STR_TO_DATE(CheckIn, '%d-%b-%Y');
UPDATE Reservations SET CheckOut = STR_TO_DATE(CheckOut, '%d-%b-%Y');