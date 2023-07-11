import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ 

CREATE TABLE odabrane_komponente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_korisnika INTEGER NOT NULL,
    id_komponente INTEGER NOT NULL,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik (id),
    FOREIGN KEY (id_komponente) REFERENCES komponenta (id)
);

"""

cur.execute(query)
con.commit()
