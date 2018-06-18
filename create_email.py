import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class CreateEmail:
	def __init__(self, sender_email, sender_password, reciever_email, subject, body, attachment):
		self.sender_email = sender_email
		self.sender_password = sender_password
		self.reciever_email = reciever_email
		self.subject = subject
		self.body = body
		self.attachment = attachment

	def send(self): #make a send list function to save processing power
		email_address = self.sender_email
		send_to_address = self.reciever_email
		password = self.sender_password
		subject = self.subject
		body = self.body

		message = MIMEMultipart()
		message["From"] = email_address
		message["To"] = send_to_address
		message["Subject"] = subject
		message.attach(MIMEText(body,"plain"))

		#MULTIMEDIA STUFF HERE
		if self.attachment == "":
			pass
		else:
			filename = self.attachment
			attachment = open(filename, "rb")
			part = MIMEBase("application", "octet-stream")
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header("Content-Disposition", "attachment; filename= " + filename)
			message.attach(part)

		try:
			text = message.as_string()
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(email_address,password)
		except:
			pass
		try:
			server.sendmail(email_address, send_to_address , text)
			return True
		except:
			return False
		server.quit()
