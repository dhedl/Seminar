CREATE TABLE komponenta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv VARCHAR(100) NOT NULL,
    cijena DECIMAL(10, 2) NOT NULL
);

CREATE TABLE procesor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    snaga INTEGER NOT NULL,
    socket VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE graficka (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    snaga INTEGER NOT NULL,
    proizvodac VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE maticna (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    socket VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE ram (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    kapacitet INTEGER NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE ssd (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    kapacitet INTEGER NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE napajanje (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_komponente INTEGER NOT NULL,
    snaga INTEGER NOT NULL,
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

CREATE TABLE korisnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime VARCHAR(100) NOT NULL,
    prezime VARCHAR(100) NOT NULL,
    telefon VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL
);

