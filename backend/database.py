import sqlite3
import os

DB_FILE = "saber_ai.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours  REAL    NOT NULL,
            sleep_hours  REAL    NOT NULL,
            mood         TEXT    NOT NULL,
            stress_risk  REAL    NOT NULL,
            burnout_risk REAL    NOT NULL,
            emotion      TEXT,
            created_at   TEXT    DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()

def save_session(data):
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sessions
            (study_hours, sleep_hours, mood, stress_risk, burnout_risk, emotion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        float(data.get("studyHours",  0)),
        float(data.get("sleepHours",  0)),
        str(data.get("mood",          "neutral")),
        float(data.get("stressRisk",  0)),
        float(data.get("burnoutRisk", 0)),
        data.get("emotion", None)
    ))
    conn.commit()
    session_id = cursor.lastrowid
    cursor.execute("SELECT * FROM sessions WHERE id = ?", (session_id,))
    row = dict(cursor.fetchone())
    conn.close()
    return row

def get_sessions():
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions ORDER BY created_at DESC LIMIT 50")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

init_db()
