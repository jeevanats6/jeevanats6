import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute(''' CREATE TABLE cars(Id INT,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',54678)")
cur.execute("INSERT INTO cars VALUES(2,'Tata',54678)")

cur.execute("INSERT INTO cars VALUES(3,'Skoda',54678)")
cur.execute("INSERT INTO cars VALUES(4,'volvo',54678)")
cur.execute("INSERT INTO cars VALUES(5,'bently',54678)")
cur.execute("INSERT INTO cars VALUES(6,'hummer',54678)")


con.commit()
print("values in table car inserted.")
