# import sqlite3
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
#
# table_query = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(table_query)
#
# connection.commit()
# connection.close()
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
# item_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(item_query)
#
# connection.commit()
# connection.close()