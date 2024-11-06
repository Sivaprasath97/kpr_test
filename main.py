import sqlite3

# Define a base User class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_db(self, conn):
        # Insert user data into the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, role) VALUES (?, ?, ?)", (self.username, self.email, 'User'))
        conn.commit()

# Define an Admin class that inherits from User
class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def save_to_db(self, conn):
        # Insert admin data into the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, role) VALUES (?, ?, ?)", (self.username, self.email, 'Admin'))
        conn.commit()

# Control Flow to determine user type
def display_user_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, role FROM users")
    users = cursor.fetchall()

    for user in users:
        username, email, role = user
        if role == 'Admin':
            print(f"Admin User: {username} - Email: {email}")
        else:
            print(f"Regular User: {username} - Email: {email}")

# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a table to store users
conn.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT NOT NULL);''')

# Create instances of User and Admin
user1 = User("john_doe", "john@example.com")
admin1 = Admin("admin_user", "admin@example.com")

# Save users to the database
user1.save_to_db(conn)
admin1.save_to_db(conn)

# Display user info based on role (Control Flow in action)
display_user_info(conn)

# Close the database connection
conn.close()
