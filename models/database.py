import sqlite3

def init_db():
    conn = sqlite3.connect('ac_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS units (id INTEGER PRIMARY KEY, location TEXT, manufacturer TEXT, model_number TEXT, serial_number TEXT, tonnage REAL, seer TEXT, heat TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY, unit_id INTEGER, issue TEXT, part TEXT, repair_status TEXT, date_repaired DATE, cost REAL)''')
    conn.commit()
    conn.close()
