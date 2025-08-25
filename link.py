import sqlite3
con = sqlite3.connect('data.bd')
c = con.cursor()

names = []
c.execute('select * from teachers')
data = c.fetchall()
for u in data :
    names.append(u[0])

name = names[-1]

