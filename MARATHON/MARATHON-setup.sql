-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE marathon (
    Place INT NOT NULL,
    MTime TIME NOT NULL,
    Pace TIME NOT NULL,
    GroupPlace INT NOT NULL,
    GroupP VARCHAR(255) NOT NULL,
    Age INT NOT NULL,
    Sex VARCHAR(255) NOT NULL,
    BIBNumber INT NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Town VARCHAR(255) NOT NULL,
    MState VARCHAR(255) NOT NULL,
    PRIMARY KEY (BIBNumber, MTime)
);