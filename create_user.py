import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = "admin"
password = "admin123"
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
if cursor.fetchone():
    print("Usuário já existe.")
else:
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, "Admin"))
    conn.commit()
    print("Usuário criado com sucesso.")

conn.close()
