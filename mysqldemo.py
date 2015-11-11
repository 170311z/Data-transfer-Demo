-*- coding: utf-8 -*-

import MySQLdb

#MySQL接続情報を渡している
connect = MySQLdb.connect(host='localhost',db='test',user='******',passwd='******')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE products (name text,price integer);''')

cursor.execute('''INSERT INTO products (name, price) VALUES ('apple', 198);''')

cursor.execute('''INSERT INTO products (name, price) VALUES ('orange', 100);''')

connection.commit()

cursor.execute('''SELECT * FROM products;''')

products = cursor.fetchall()
print(products) # -> (('apple', 198L), ('orange', 100L))
