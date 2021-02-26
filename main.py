import sqlite3

active = True

conn = sqlite3.connect("cards.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS "
            "cards (name text, "
            "setName text, "
            "setCode text, "
            "setNum integer, "
            "manaCost text, "
            "cmc integer"
            "cardText text, "
            "flavourText text, "
            "quantity integer)")

while active:
    userInput = input("\nPlease enter a card name to add, 'quit' or 'all':")
    if userInput == 'quit' or userInput == 'q':
        active = False
    elif userInput == 'all' or userInput == 'a':
        cur.execute("SELECT * FROM cards")
        rows = cur.fetchall()
        for row in rows:
            print("Card Name: " + row[0] + " --- "
                  "Set Name: " + row[1] + " --- "
                  "Set Code: " + row[2] + " --- "
                  "Number in Set: " + str(row[3]) + " --- "
                  "Mana Cost: " + row[4] + " --- " 
                  "Converted Mana Cost: " + str(row[5]) + " --- "
                  "Card Text: " + row[6] + " --- "
                  "Flavour Text: " + row[7] + " --- " +
                  "Quantity: " + row[8])
    else:
        cur.execute("INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (userInput, "n", "code", 0, "cost", 0, "c", "f", 0))
