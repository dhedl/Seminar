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

CREATE TABLE odabrane_komponente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_korisnika INTEGER NOT NULL,
    komponente TEXT NOT NULL,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik (id)
);

-- Procesor
INSERT INTO komponenta (naziv, cijena) VALUES ('Intel Core i5-13600K', 384.74);
INSERT INTO procesor (id_komponente, snaga, socket) VALUES (1, 125, 'Intel 1700');


INSERT INTO komponenta (naziv, cijena) VALUES ('AMD Ryzen 7 5800X', 247.37);
INSERT INTO procesor (id_komponente, snaga, socket) VALUES (2, 105, 'AMD AM4');


-- Grafička kartica
INSERT INTO komponenta (naziv, cijena) VALUES ('NVIDIA GeForce RTX 4070Ti', 1262.11);
INSERT INTO graficka (id_komponente, snaga, proizvodac) VALUES (3, 285, 'ASUS ROG STRIX');

INSERT INTO komponenta (naziv, cijena) VALUES ('AMD Radeon RX 7900 XT', 1138.95);
INSERT INTO graficka (id_komponente, snaga, proizvodac) VALUES (4, 230, 'ASUS TUF');


-- Matična ploča
INSERT INTO komponenta (naziv, cijena) VALUES ('ASUS ROG MAXIMUS Z690 EXTREME', 1347.37);
INSERT INTO maticna (id_komponente, socket) VALUES (5, 'Intel 1700');

INSERT INTO komponenta (naziv, cijena) VALUES ('ASUS ROG CROSSHAIR VIII EXTREME X570', 910.00);
INSERT INTO maticna (id_komponente, socket) VALUES (6, 'AMD AM4');


-- RAM memorija
INSERT INTO komponenta (naziv, cijena) VALUES ('Kingston Fury Best 5600MHz 64GB (2x32GB)', 247.37);
INSERT INTO ram (id_komponente, kapacitet) VALUES (7, 16);

INSERT INTO komponenta (naziv, cijena) VALUES ('G.SKILL Trident Z Neo 3600MHz 32GB (2x16GB)', 89.99);
INSERT INTO ram (id_komponente, kapacitet) VALUES (8, 32);


-- SSD disk
INSERT INTO komponenta (naziv, cijena) VALUES ('Samsung 980 PRO 1TB', 89.99);
INSERT INTO ssd (id_komponente, kapacitet) VALUES (9, 1000);

INSERT INTO komponenta (naziv, cijena) VALUES ('Crucial MX500 500GB', 64.99);
INSERT INTO ssd (id_komponente, kapacitet) VALUES (10, 500);


-- Napajanje
INSERT INTO komponenta (naziv, cijena) VALUES ('Seasonic PRIME Tx-1300', 505.26);
INSERT INTO napajanje (id_komponente, snaga) VALUES (11, 1300);

INSERT INTO komponenta (naziv, cijena) VALUES ('Corsair HX1500i', 372.64);
INSERT INTO napajanje (id_komponente, snaga) VALUES (12, 1500);
