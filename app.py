import sqlite3

connection = sqlite3.connect('my-database.db')

cursor = connection.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS Products
               (product_id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, supplier TEXT, price_per_tonne INT) ''')

products_to_insert = [
  ('Bananas', 'United Bananas', 7000),
  ('Avocardos', 'United Avocardos', 12000),
]

# cursor.executemany('''
# INSERT INTO Products(product, supplier, price_per_tonne)
# VALUES (?,?,?)
# ''', products_to_insert)

cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())


cursor.execute("SELECT supplier FROM Products")
print(cursor.fetchall())

price = (12000,)
cursor.execute("SELECT * FROM Products WHERE price_per_tonne=?", price)
print(cursor.fetchall())


united_fruit_price = (7000,)
cursor.execute("UPDATE Products SET supplier='United Fruits' WHERE price_per_tonne=?", united_fruit_price)
print(cursor.fetchall())

cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())


cursor.execute("DELETE FROM Products WHERE product_id=2")
cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())


connection.commit()
connection.close()