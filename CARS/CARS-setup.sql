-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE Continents (
    ContId INT PRIMARY KEY,
    Continent VARCHAR(255) NOT NULL
);

CREATE TABLE Countries (
    CountryId INT PRIMARY KEY,
    CountryName VARCHAR(255) NOT NULL,
    ContId INT NOT NULL,
    FOREIGN KEY (ContId) REFERENCES Continents(ContId)
);

CREATE TABLE CarMakers (
    Id INT PRIMARY KEY,
    Maker VARCHAR(255) NOT NULL,
    FullName VARCHAR(255) NOT NULL,
    CountryId INT NOT NULL,
    FOREIGN KEY (CountryId) REFERENCES Countries(CountryId)
);

CREATE TABLE ModelList (
    ModelId INT PRIMARY KEY,
    Maker INT NOT NULL,
    Model VARCHAR(255) NOT NULL,
    FOREIGN KEY (Maker) REFERENCES CarMakers(Id)
);

CREATE TABLE CarNames (
    MakeId INT PRIMARY KEY,
    Model VARCHAR(255) NOT NULL,
    MakeDescription VARCHAR(255) NOT NULL
);

CREATE TABLE CarsData (
    Id INT,
    MPG INT,
    Cylinders INT,
    Edispl INT,
    Horsepower INT,
    Weight INT,
    Accelerate FLOAT,
    Year INT,
    PRIMARY KEY (Id),
    FOREIGN KEY (Id) REFERENCES CarNames(MakeId)
);