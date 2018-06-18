import sqlite3

class NewAutofill:
	def __init__(self, email_address):
		self.email_address = email_address

	def add_to_db(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_autofill(email_address VARCHAR)")
		c.execute("INSERT INTO registered_autofill(email_address) VALUES(?)",
			(self.email_address,))
		conn.commit()
		c.close()
		conn.close()

class OldAutofill:
	def load_autofill(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_autofill(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_autofill")
		all_email_addresses = []
		for row in c.fetchall():
			all_email_addresses.append(row[0])
		c.close()
		conn.close()
		return all_email_addresses

	def delete_autofill(self, email_address):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_autofill(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_autofill")
		c.execute("DELETE FROM registered_autofill where email_address = (?)",
			(email_address,))

		#delete default if it was the item deleted
		c.execute("SELECT * FROM default_autofill")
		try:
			default_autofill = c.fetchall()[0][0]
			if default_autofill == email_address:

				c.execute("DELETE FROM default_autofill")
		except:
			pass
		conn.commit()
		c.close()
		conn.close()
			

	def edit_autofill(self, email_address, updated_email_address):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_autofill(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_autofill")
		c.execute("UPDATE registered_autofill SET email_address = (?) WHERE email_address = (?)",
			(updated_email_address, email_address))
		conn.commit()
		c.close()
		conn.close()
		
class DefaultAutofill:
	def set_new_autofill(self, email_address):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS default_autofill(email_address TEXT)")
		c.execute("DELETE FROM default_autofill")
		c.execute("INSERT INTO default_autofill(email_address) VALUES(?)",
			(email_address,))
		conn.commit()
		c.close()
		conn.close()
	def edit_default_autofill(self, email_address, updated_email_address):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS default_autofill(email_address TEXT)")
		c.execute("SELECT * FROM default_autofill")
		c.execute("UPDATE default_autofill SET email_address = (?) WHERE email_address = (?)",
			(updated_email_address, email_address))
		conn.commit()
		c.close()
		conn.close()
