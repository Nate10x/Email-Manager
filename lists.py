import sqlite3

class NewList:
	def __init__(self, name, email_addresses):
		self.name = name
		self.email_address  = email_addresses

	def add_to_db(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("INSERT INTO registered_lists(name, email_addresses) VALUES(?,?)",
			(self.name, self.email_address))
		conn.commit()
		c.close()
		conn.close()

class OldLists:
	def load_list_names(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("SELECT name FROM registered_lists")
		all_lists = []
		for row in c.fetchall():
			all_lists.append(row)
		c.close()
		conn.close()
		return all_lists

	def load_list_objects(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("SELECT * FROM registered_lists")
		all_lists = []
		for row in c.fetchall():
			all_lists.append(row)
		c.close()
		conn.close()
		return all_lists

	def load_this_list(self, name):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("SELECT email_addresses FROM registered_lists WHERE name = (?)",
			(name,))
		string_of_email_adresses = c.fetchall()
		c.close()
		conn.close()
		return string_of_email_adresses	

	def edit_list(self, name, new_email_addresses):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("SELECT * FROM registered_lists")
		c.execute("UPDATE registered_lists SET email_addresses = (?) WHERE name = (?)",
			(new_email_addresses, name))
		conn.commit()
		c.close()
		conn.close()

	def delete_list(self, name):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_lists(name VARCHAR, email_addresses TEXT)")
		c.execute("SELECT * FROM registered_lists")
		c.execute("DELETE FROM registered_lists where name = (?)",
			(name,))
		conn.commit()
		c.close()
		conn.close()
