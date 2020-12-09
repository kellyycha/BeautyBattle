import sqlite3

#easy leaderboard
conn = sqlite3.connect('data/easyLeaderboard.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE easyLeaderboard(
    Username TEXT,
    Score INTEGER,
    Time TEXT
    )""")

#medium leaderboard
conn = sqlite3.connect('data/mediumLeaderboard.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE mediumLeaderboard(
    Username TEXT,
    Score INTEGER,
    Time TEXT
    )""")

#hard leaderboard
conn = sqlite3.connect('data/hardLeaderboard.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE hardLeaderboard(
    Username TEXT,
    Score INTEGER,
    Time TEXT
    )""")

conn.commit()
conn.close()