#to send sql code to data base
import sqlite3
import psycopg2

#post sql data base

def create_table():
    #Create a connection
    con = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'Dexter99' host = 'localhost' port = '5432'") #pass database file #if not created it will be passed by this line of code
    #cursor object
    cur = con.cursor()
    #sql 
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit() #to update it
    con.close()

def insert (item, quantity, price):
    con = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'Dexter99' host = 'localhost' port = '5432'")
    cur = con.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" %(item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)",  (item, quantity, price))
    con.commit()
    con.close()

def view ():
    #to establish connection with database
    con = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'Dexter99' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("SELECT * from STORE")
    rows = cur.fetchall()
    con.close()
    return rows

def delete (item):
    con = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'Dexter99' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute ("DELETE FROM store WHERE item =%s", (item,))
    con.commit()
    con.close()

def update (quantity, price, item):
    con = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'Dexter99' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute ("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item)) #setting quantity&price/only where these rows where item = given value
    con.commit()
    con.close()

#update(11,6, "Water glass")
#insert("Coffee cup", 10, 5)
#delete("Wine Glass")
#print(view())

create_table()
#insert("Orange", 10, 15)
#delete("Orange")
update(20, 15, "Apple")
print(view())