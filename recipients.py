import sqlite3

class NewRecipient:
	def __init__(self, email_address):
		self.email_address = email_address

	def add_to_db(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_email_addresses(email_address VARCHAR)")
		c.execute("INSERT INTO registered_email_addresses(email_address) VALUES(?)",
			(self.email_address,))
		conn.commit()
		c.close()
		conn.close()

class OldRecipients:
	def load_recipients(self):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_email_addresses(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_email_addresses")
		all_email_addresses = []
		for row in c.fetchall():
			all_email_addresses.append(row[0])
		c.close()
		conn.close()
		return all_email_addresses

	def delete_recipient(self, recipient):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_email_addresses(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_email_addresses")
		c.execute("DELETE FROM registered_email_addresses where email_address = (?)",
			(recipient,))
		conn.commit()
		c.close()
		conn.close()

	def edit_recipient(self, recipient, updated_recipient):
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS registered_email_addresses(email_address VARCHAR)")
		c.execute("SELECT * FROM registered_email_addresses")
		c.execute("UPDATE registered_email_addresses SET email_address = (?) WHERE email_address = (?)",
			(updated_recipient, recipient))
		conn.commit()
		c.close()
		conn.close()
		



