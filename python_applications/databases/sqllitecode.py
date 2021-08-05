#to send sql code to data base
import sqlite3
import sqlite3

#post sql data base
#sqlite3


#execute() means 



def create_table():
    #Create a connection
    con = sqlite3.connect("lite.db") #pass database file #if not created it will be passed by this line of code
    #cursor object
    cur = con.cursor()
    #sql 
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #creating table with these as columns if it doesn't exists
    con.commit() #to update it
    con.close()

def insert (item, quantity, price):
    con = sqlite3.connect("lite.db") #need to connect to server
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?,)",(item, quantity, price))
    con.commit()
    con.close()

def view ():
    #to establish connection with database
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    con.close()
    return rows

def delete (item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute ("DELETE FROM store WHERE item =?", (item,))
    con.commit()
    con.close()

def update (quantity, price, item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute ("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item)) #setting quantity&price/only where these rows where item = given value
    con.commit()
    con.close()

update(11,6, "Water glass")
#insert("Coffee cup", 10, 5)
delete("Wine Glass")

for x in range (0,11,1):
    delete("Coffee cup") #delete from server

printedstore = view()
for item in printedstore:
    print(item)