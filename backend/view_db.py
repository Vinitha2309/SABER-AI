
import sqlite3

# Open the database
conn   = sqlite3.connect("saber_ai.db")
cursor = conn.cursor()

# ── Show all table names ──────────────────────
print("\n📂 Tables in database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for table in tables:
    print("  →", table[0])

# ── Show all sessions ─────────────────────────
print("\n📊 All Sessions:")
print("-" * 80)
cursor.execute("SELECT * FROM sessions ORDER BY created_at DESC")
rows = cursor.fetchall()

if not rows:
    print("  No sessions found yet.")
else:
    print(f"  {'ID':<5} {'Study':<8} {'Sleep':<8} {'Mood':<10} {'Stress':<10} {'Burnout':<10} {'Date'}")
    print("  " + "-" * 70)
    for row in rows:
        print(f"  {row[0]:<5} {row[1]:<8} {row[2]:<8} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[7]}")

print(f"\n  Total records: {len(rows)}")

conn.close()
