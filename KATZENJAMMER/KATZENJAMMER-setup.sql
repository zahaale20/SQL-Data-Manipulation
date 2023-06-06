-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE Albums (
    AId INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Year INT NOT NULL,
    Label VARCHAR(255) NOT NULL,
    Typee VARCHAR(255)
);

CREATE TABLE Songs (
    SongId INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL
);

CREATE TABLE Band (
    Id INT PRIMARY KEY,
    Firstname VARCHAR(255) NOT NULL,
    Lastname VARCHAR(255) NOT NULL
);

CREATE TABLE Vocals (
    SongId INT NOT NULL,
    Bandmate INT NOT NULL,
    Type VARCHAR(255) NOT NULL,
    PRIMARY KEY (SongId, Bandmate, Type),
    FOREIGN KEY (SongId) REFERENCES Songs(SongId),
    FOREIGN KEY (Bandmate) REFERENCES Band(Id)
);

CREATE TABLE Instruments (
    SongId INT NOT NULL,
    BandmateId INT NOT NULL,
    Instrument VARCHAR(255) NOT NULL,
    PRIMARY KEY (SongId, BandmateId, Instrument),
    FOREIGN KEY (SongId) REFERENCES Songs(SongId),
    FOREIGN KEY (BandmateId) REFERENCES Band(Id)
);

CREATE TABLE Performance (
    SongId INT NOT NULL,
    Bandmate INT NOT NULL,
    StagePosition VARCHAR(255) NOT NULL,
    PRIMARY KEY (SongId, Bandmate),
    FOREIGN KEY (SongId) REFERENCES Songs(SongId),
    FOREIGN KEY (Bandmate) REFERENCES Band(Id)
);

CREATE TABLE Tracklists (
    AlbumId INT NOT NULL,
    Position INT NOT NULL,
    SongId INT NOT NULL,
    PRIMARY KEY (AlbumId, Position),
    FOREIGN KEY (AlbumId) REFERENCES Albums(AId),
    FOREIGN KEY (SongId) REFERENCES Songs(SongId)
);