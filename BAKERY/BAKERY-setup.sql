-- Alex Zaharia
-- azaharia@calpoly.edu
-- May 2, 2023


CREATE TABLE customers (
    Id INT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL
);

CREATE TABLE goods (
    Id VARCHAR(255) PRIMARY KEY,
    Flavor VARCHAR(255) NOT NULL,
    Food VARCHAR(255) NOT NULL,
    Price FLOAT NOT NULL,
    UNIQUE KEY (Id)
);

CREATE TABLE receipts (
    ReceiptNumber INT PRIMARY KEY,
    Date DATE NOT NULL,
    CustomerId INT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES customers(Id)
) DEFAULT CHARSET=utf8;

ALTER TABLE receipts MODIFY COLUMN Date DATE NOT NULL DEFAULT '0000-00-00';

SET sql_mode = '';
ALTER TABLE receipts MODIFY COLUMN Date VARCHAR(15) NOT NULL DEFAULT '';

UPDATE receipts SET Date = STR_TO_DATE(Date, '%d-%b-%Y');

CREATE TABLE items (
    Receipt INT NOT NULL,
    Ordinal INT NOT NULL,
    Item VARCHAR(255) NOT NULL,
    PRIMARY KEY (Receipt, Ordinal),
    FOREIGN KEY (Receipt) REFERENCES receipts(ReceiptNumber),
    FOREIGN KEY (Item) REFERENCES goods(Id)
);
