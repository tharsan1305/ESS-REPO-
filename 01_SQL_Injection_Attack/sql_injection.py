import sqlite3

# Create database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create user table
cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

# Insert sample records
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
cursor.execute("INSERT INTO users VALUES ('student', 'pass123')")

print("===== SQL INJECTION ATTACK =====")

# Get user input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Vulnerable SQL query
query = (
    "SELECT * FROM users WHERE username = '"
    + username
    + "' AND password = '"
    + password
    + "'"
)

print("\nGenerated SQL Query:")
print(query)

# Execute vulnerable query
cursor.execute(query)
result = cursor.fetchall()

if result:
    print("\nLogin Successful!")
    print("User Records:", result)
else:
    print("\nInvalid Username or Password")

# Secure parameterized query
print("\n===== SECURE LOGIN =====")

cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)

secure_result = cursor.fetchall()

if secure_result:
    print("Secure Login Successful!")
else:
    print("Secure Login Failed!")

conn.close()

