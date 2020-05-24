import sqlite3

conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute("SELECT rowid, todo FROM todos")
# c.execute("UPDATE todos SET todo = 'My First Task' WHERE rowid = 1")
todos = c.fetchall()

print(todos)

# for t in todos:
#     print(t[1])


conn.commit()
conn.close()