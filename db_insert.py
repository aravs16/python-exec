import sqlite3
todo = input("Enter todo: ")
conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute("INSERT INTO todos VALUES ('"+todo+"')")
print(todo, "is inserted")
conn.commit()
conn.close()