import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ 

INSERT INTO _________ VALUES
    

"""

cur.execute(query)
con.commit()
