import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ 

SELECT * FROM komponenta INNER JOIN graficka ON komponenta.id = graficka.id_komponente;

"""

data = cur.execute(query).fetchall()

for d in data:
    print(d)
