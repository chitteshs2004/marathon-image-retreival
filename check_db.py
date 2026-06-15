import sqlite3
import os

db_path = "OCR/OCR/my_database.db"
print(f"DB exists: {os.path.exists(db_path)}, size: {os.path.getsize(db_path)} bytes")

conn = sqlite3.connect(db_path)
c = conn.cursor()

tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(f"Tables: {tables}")

for (t,) in tables:
    count = c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {count} rows")
    if count > 0:
        sample = c.execute(f"SELECT * FROM {t} LIMIT 5").fetchall()
        print(f"  Sample rows: {sample}")

conn.close()

# Also check AWS creds
print("\n--- AWS Config in ocr.py ---")
with open("OCR/OCR/ocr.py") as f:
    for i, line in enumerate(f):
        if "AWS" in line and "environ" in line:
            print(f"  Line {i+1}: {line.strip()}")
