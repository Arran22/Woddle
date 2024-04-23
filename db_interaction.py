import sqlite3

class database_manager:
    def __init__(self, db_name='PokeMart.db'):
        # Connect to the database (creates a new database if it doesn't exist)
        self.conn = sqlite3.connect(db_name)

        # Create a cursor object to execute SQL queries
        self.cursor = self.conn.cursor()

        # Create a table for users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                wins NUMBER DEFAULT 0 NOT NULL
            )
        ''')

        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        users = self.cursor.fetchall()
        return users

    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        users = self.cursor.fetchall()
        return users

    def get_user_by_name(self, username):
        self.cursor.execute("SELECT * FORM users WHERE username = ?", (username,))
        users = self.cursor.fetchall()
        return users
    
    def drop_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def update_user_wins(self, id, wins):
        self.cursor.execute("UPDATE users SET wins = ? WHERE id = ?", (wins, id))