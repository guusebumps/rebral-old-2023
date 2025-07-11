import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users")
conn.commit()

print("Todos os usuários foram removidos com sucesso.")
conn.close()
