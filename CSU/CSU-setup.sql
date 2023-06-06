-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE Campuses(
    Id INT,
    Campus VARCHAR(255),
    Location VARCHAR(255),
    County  VARCHAR(255),
    Year INT,
    PRIMARY KEY (Id),
    UNIQUE (Campus)
);

CREATE TABLE CSUFees(
    Campus INT,
    Year INT,
    CampusFee INT,
    PRIMARY KEY (Campus, Year)
);

CREATE TABLE Degrees(
    Campus INT,
    Year INT,
    Degrees INT
);

CREATE TABLE Disciplines (
    Id INT PRIMARY KEY,
    DisciplineName VARCHAR(255),
    UNIQUE (DisciplineName)
);

CREATE TABLE DisciplineEnrollments (
    CampusId INT NOT NULL,
    DisciplineId INT NOT NULL,
    AcademicYear INT NOT NULL,
    UndergradEnrollment INT NOT NULL,
    GradEnrollment INT NOT NULL,
    FOREIGN KEY(CampusId) REFERENCES Campuses(Id),
    FOREIGN KEY(DisciplineId) REFERENCES Disciplines(Id),
    PRIMARY KEY (CampusId, DisciplineId, AcademicYear)
);

CREATE TABLE Enrollments (
    CampusId INT NOT NULL,
    AcademicYear INT NOT NULL,
    TotalEnrollment INT NOT NULL,
    FTE INT NOT NULL,
    FOREIGN KEY (CampusId) REFERENCES Campuses(Id),
    PRIMARY KEY (CampusId, AcademicYear)
);

CREATE TABLE Faculty (
    CampusId INT NOT NULL,
    AcademicYear INT NOT NULL,
    NumFaculty FLOAT NOT NULL,
    FOREIGN KEY (CampusId) REFERENCES Campuses(Id),
    PRIMARY KEY (CampusId, AcademicYear)
);