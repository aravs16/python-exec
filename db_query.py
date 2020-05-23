import sqlite3

conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute("SELECT rowid, todo FROM todos")
todos = c.fetchall()

# print(todos)

for t in todos:
    print(t[1])


conn.commit()
conn.close()