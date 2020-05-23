import sqlite3

conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute('''CREATE TABLE todos
             (todo text)''')
conn.commit()
conn.close()