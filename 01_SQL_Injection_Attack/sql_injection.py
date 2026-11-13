
import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE users(username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES('admin', '1234')")

print("1. Vulnerable Login")
print("2. Secure Login")

choice = input("Enter choice: ")

username = input("Enter username: ")
password = input("Enter password: ")

if choice == "1":
    query = (
        "SELECT * FROM users WHERE username='"
        + username +
        "' AND password='" + password + "'"
    )
    cur.execute(query)

elif choice == "2":
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cur.execute(query, (username, password))

else:
    print("Invalid choice")
    con.close()
    exit()

if cur.fetchone():
    print("Login Successful")
else:
    print("Login Failed")

con.close()
