-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023

CREATE TABLE appellations (
  Num INT PRIMARY KEY,
  Appellation VARCHAR(255),
  County VARCHAR(255),
  AState VARCHAR(255),
  Area VARCHAR(255),
  isAVA VARCHAR(255)
);

CREATE TABLE grapes (
  GrapeID INTEGER PRIMARY KEY,
  Grape VARCHAR(255),
  Color VARCHAR(255)
);

CREATE TABLE wine (
  Num INTEGER PRIMARY KEY,
  Grape VARCHAR(255),
  Winery VARCHAR(255),
  Appellation VARCHAR(255),
  WState VARCHAR(255),
  WName VARCHAR(255),
  WYear INTEGER,
  Price INTEGER,
  Score INTEGER,
  Cases INTEGER,
  Drink VARCHAR(255),
  FOREIGN KEY (Grape) REFERENCES grapes(Grape),
  FOREIGN KEY (WState) REFERENCES appelations(AState)
);
