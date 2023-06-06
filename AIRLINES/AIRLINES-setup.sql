-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE airlines (
    Id INT PRIMARY KEY,
    Airline VARCHAR(255) NOT NULL,
    Abbreviation VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL
);

CREATE TABLE airports100 (
    City VARCHAR(255) NOT NULL,
    AirportCode VARCHAR(3) PRIMARY KEY,
    AirportName VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    CountryAbbrev VARCHAR(255) NOT NULL
);

CREATE TABLE flights (
    Airline INT NOT NULL,
    FlightNo INT NOT NULL,
    SourceAirport VARCHAR(3) NOT NULL,
    DestAirport VARCHAR(3) NOT NULL,
    PRIMARY KEY (Airline, FlightNo, SourceAirport),
    FOREIGN KEY (Airline) REFERENCES airlines(Id),
    FOREIGN KEY (SourceAirport) REFERENCES airports100(AirportCode),
    FOREIGN KEY (DestAirport) REFERENCES airports100(AirportCode)
);