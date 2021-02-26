import sqlite3

active = True

conn = sqlite3.connect("cards.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE cards (name)")

while active:
    userInput = input("\nPlease enter a card name to add, 'quit' or 'all':")
    if userInput == 'quit' or userInput == 'q':
        active = False
    elif userInput == 'all' or userInput == 'a':
        cur.execute("SELECT * FROM cards")
        rows = cur.fetchall()
        for row in rows:
            print("Name: " + row[0])
    else:
        cur.execute("INSERT INTO cards VALUES (?)", [userInput])
