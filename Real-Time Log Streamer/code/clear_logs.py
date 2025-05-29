# clear_logs.py
import sqlite3

conn = sqlite3.connect('logs.db')
c = conn.cursor()

c.execute("DELETE FROM logs")

# rows = c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 20").fetchall()

# for row in rows:
#     print(row)

conn.commit()

print("✅ logs.db cleared.")

conn.close()
