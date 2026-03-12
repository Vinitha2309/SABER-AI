import sqlite3

conn   = sqlite3.connect("saber_ai.db")
cursor = conn.cursor()

# ── Find high stress sessions ─────────────────
print("\n🔴 High Stress Sessions (stress > 60%):")
cursor.execute("SELECT * FROM sessions WHERE stress_risk > 60 ORDER BY created_at DESC")
rows = cursor.fetchall()
for row in rows:
    print(f"  ID:{row[0]} | Stress:{row[4]}% | Burnout:{row[5]}% | Mood:{row[3]} | Date:{row[7]}")

# ── Find sessions by mood ─────────────────────
print("\n😔 Sad Mood Sessions:")
cursor.execute("SELECT * FROM sessions WHERE mood = 'sad'")
rows = cursor.fetchall()
for row in rows:
    print(f"  ID:{row[0]} | Study:{row[1]}hrs | Sleep:{row[2]}hrs | Stress:{row[4]}%")

# ── Count total sessions ──────────────────────
cursor.execute("SELECT COUNT(*) FROM sessions")
total = cursor.fetchone()[0]
print(f"\n📈 Total sessions recorded: {total}")

# ── Average stress risk ───────────────────────
cursor.execute("SELECT AVG(stress_risk) FROM sessions")
avg = cursor.fetchone()[0]
if avg:
    print(f"📊 Average stress risk: {avg:.1f}%")

conn.close()
