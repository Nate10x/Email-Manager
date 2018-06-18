from tkinter import filedialog
from create_email import CreateEmail
from recipients import NewRecipient, OldRecipients
from autofill import NewAutofill, OldAutofill, DefaultAutofill
from lists import NewList, OldLists
from my_globals import *


class EmailGUI(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('Email Manager')
		tk.Tk.iconbitmap(self, default = r'C:\Users\nate one\Pictures\PythonPics\myLogo.ico')
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		bottom = tk.Frame(self)
		bottom.pack(side="bottom", fill="x", padx=(7,0), pady=(0, 5))

		GlobalWidget.status_label = tk.Label(bottom, text="", fg="red", anchor="w")
		GlobalWidget.status_label.grid(column=10, row=10)

		self.frames = {}

		for F in (StartPage, RecipientsPage, ListsPage, AutofillPage, PrewritePage):
			frame = F(container, self)
			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)	

	def show_frame(self, cont):
		GlobalWidget.status_label.config(text="")
		frame = self.frames[cont]
		frame.tkraise()


class SetFramesAndNavBar:
	def __init__(self, main_frame, current_page, controller):

		myColor = "black" 
		startpage_butt_color = None
		recipientspage_butt_color = None
		listspage_butt_color = None
		autofillpage_butt_color = None
		prewritepage_butt_color = None

		if current_page == "StartPage":
			startpage_butt_color = myColor
		elif current_page == "RecipientsPage":
			recipientspage_butt_color = myColor
		elif current_page == "ListsPage":
			listspage_butt_color = myColor
		elif current_page == "AutofillPage":
			autofillpage_butt_color = myColor
		elif current_page == "PrewritePage":
			prewritepage_butt_color = myColor

		else:
			GlobalWidget.status_label.config(fg="red")
			GlobalWidget.status_label.config(text="unknown error")

		self.top = tk.Frame(main_frame)
		self.top.pack(fill="x")

		navbar_frame = tk.Frame(self.top, bg="powder blue", bd=12, relief="raised")

		home_butt = tk.Button(navbar_frame, font=navbar_button_font, text="Home", fg=nav_button_fg, bg=startpage_butt_color, command=lambda: controller.show_frame(StartPage))
		home_butt.grid(column=10, row=10, padx=(30,0), pady=nav_butt_pady, sticky="w")
		
		recipients_butt = tk.Button(navbar_frame, font=navbar_button_font, text="Recipients", fg=nav_button_fg, bg=recipientspage_butt_color, command=lambda: controller.show_frame(RecipientsPage))
		recipients_butt.grid(column=11, row=10, padx=nav_butt_padx, pady=nav_butt_pady)

		lists_butt = tk.Button(navbar_frame, font=navbar_button_font, text="Lists", fg=nav_button_fg, bg=listspage_butt_color, command=lambda: controller.show_frame(ListsPage))
		lists_butt.grid(column=12, row=10, padx=nav_butt_padx, pady=nav_butt_pady)

		autofill_butt = tk.Button(navbar_frame, font=navbar_button_font, text="Autofill", fg=nav_button_fg, bg=autofillpage_butt_color, command=lambda: controller.show_frame(AutofillPage))
		autofill_butt.grid(column=13, row=10, padx=nav_butt_padx, pady=nav_butt_pady)

		prewrite_butt = tk.Button(navbar_frame, font=navbar_button_font, text="Prewrite", fg=nav_button_fg, bg=prewritepage_butt_color, command=lambda: controller.show_frame(PrewritePage))
		prewrite_butt.grid(column=14, row=10, padx=(30,30), pady=nav_butt_pady)

		navbar_frame.pack(fill="x", side="top", anchor="n")

		self.middle = tk.Frame(main_frame)
		self.middle.pack(padx=(10,10))

	

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#self.controller = controller

		page = SetFramesAndNavBar(self, "StartPage", controller)

		# ~~~~~EMAIL_FRAME~~~~~
		email_frame = tk.LabelFrame(page.middle, font=frame_title_font, text="Send An Email", bd=5, fg=frame_title_color)
		
		GlobalWidget.to_var = tk.StringVar()
		from_var = tk.StringVar()
		password_var = tk.StringVar()
		subject_var = tk.StringVar()
		path_var = tk.StringVar()

		to_label = tk.Label(email_frame, font=email_page_font, text="Send To:")
		to_label.grid(column=10, row=10, sticky="w", padx=widget_padx, pady=widget_pady)

		to_entry = tk.Entry(email_frame, textvariable=GlobalWidget.to_var, font=email_page_font, bg=entries_bg, width=entry_width)
		to_entry.grid(column=11, row=10, padx=widget_padx, pady=widget_pady)

		from_label = tk.Label(email_frame, font=email_page_font, text="Sent From:")
		from_label.grid(column=10, row=11, sticky="w", padx=widget_padx, pady=widget_pady)

		from_frame = tk.Frame(email_frame)
		from_frame.grid(column=11, row=11, padx=widget_padx, pady=widget_pady)

		from_entry = tk.Entry(from_frame, textvariable=from_var, font=email_page_font, bg=entries_bg, width=entry_width-5)
		from_entry.grid(column=10, row=10, sticky="w")

		def insert_autofill():
			from_var.set(GlobalWidget.CURRENT_AUTOFILL)


		autofill_butt = tk.Button(from_frame, font=email_page_autofill_font, width=5, height=1, text="Autofill", bd=5, bg=buttons_bg, command=insert_autofill)
		autofill_butt.grid(column=11, row=10)

		password_label = tk.Label(email_frame, font=email_page_font, text="Password:")
		password_label.grid(column=10, row=12, sticky="w", padx=widget_padx, pady=widget_pady)

		password_entry = tk.Entry(email_frame, textvariable=password_var, font=email_page_font, width=entry_width, bg=entries_bg, show="*")
		password_entry.grid(column=11, row=12, padx=widget_padx, pady=widget_pady)

		subject_label = tk.Label(email_frame, font=email_page_font, text="Subject:")
		subject_label.grid(column=10, row=13, sticky="w", padx=widget_padx, pady=widget_pady)

		subject_entry = tk.Entry(email_frame, textvariable=subject_var, font=email_page_font, bg=entries_bg, width=entry_width)
		subject_entry.grid(column=11, row=13, padx=widget_padx, pady=widget_pady)

		body_label = tk.Label(email_frame, font=email_page_font, text="Body:")
		body_label.grid(column=10, row=14, sticky="nw", padx=widget_padx, pady=widget_pady)

		body_text = tk.Text(email_frame, font=email_page_body_font, width=txt_width, height=txt_height, bg=entries_bg)
		body_text.grid(column=11, row=14, padx=b_widget_padx, pady=b_widget_pady)

		browse_label = tk.Label(email_frame, font=email_page_font, text="Attach File:")
		browse_label.grid(column=10, row=15, sticky="nw", padx=widget_padx, pady=widget_pady)


		partial_browse_frame = tk.Frame(email_frame)
		partial_browse_frame.grid(column=11, row=15, padx=browse_padx, pady=browse_pady, sticky="w")

		def getPath():
			PATH = filedialog.askopenfilename()
			path_entry.config(state="normal")
			path_entry.delete(0, "end")
			path_entry.insert(0, PATH)
			path_entry.config(state="disabled")
			path_var.set(PATH)

		browse_butt = tk.Button(partial_browse_frame, font=email_page_font, text="Browse", bg=buttons_bg, command=getPath)
		browse_butt.grid(column=10, row=10)

		path_entry = tk.Entry(partial_browse_frame, textvariable=path_var, font=email_page_path_font, text="Path:", bg="grey92", width=24, state="disabled")
		path_entry.grid(column=11, row=10)

		def get_and_send(body_text):
			error_occured = False
			#here to write if statement for sending email lists :)
			try:

				to_entry = GlobalWidget.to_var.get() 
				if to_entry[0] == "<" and to_entry[1] == "[" and to_entry[-1] == ">" and to_entry[-2] == "]":
					list_name = [char for char in to_entry if char not in ('<', '[', ']', '>')]
					list_name = ''.join(list_name)
					
					list_recipients = OldLists()
					long_string_of_recipients = list_recipients.load_this_list(list_name)[0][0]
					list_of_recipients = long_string_of_recipients.split("<[seperator]>")
					for recipient in list_of_recipients:
						myEmail = CreateEmail(from_var.get(), password_var.get(), recipient, subject_var.get(), body_text.get("1.0", 'end-1c'), path_var.get())
						sent = myEmail.send()
						if not sent:
							error_occured = True
					if error_occured == True:
						GlobalWidget.status_label.config(fg="red")
						GlobalWidget.status_label.config(text="An error occured when sending emails to " + "'" + list_name + "'.")
					else:
						GlobalWidget.status_label.config(fg="green")
						GlobalWidget.status_label.config(text="Email sent to all recipients in list " + "'" + list_name + "'.")
					


				else:
					myEmail = CreateEmail(from_var.get(), password_var.get(), GlobalWidget.to_var.get(), subject_var.get(), body_text.get("1.0", 'end-1c'), path_var.get())
					sent = myEmail.send()
					if sent:
						GlobalWidget.status_label.config(fg="green")
						GlobalWidget.status_label.config(text="Email sent to " + GlobalWidget.to_var.get())
					else:
						GlobalWidget.status_label.config(fg="red")
						GlobalWidget.status_label.config(text="Error sending email to '" + GlobalWidget.to_var.get() + "', please check your spelling.")
					
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please do not leave required fileds blank ('To', 'From', and 'Password').")

		bottom_buttons_frame = tk.Frame(email_frame)
		bottom_buttons_frame.grid(column=10, row=16, columnspan=2, sticky="e", padx=butt_padx, pady=butt_pady)

		def cancel_file():
			path_var.set("")
			path_entry.config(state="normal")
			path_entry.delete(0, "end")
			path_entry.config(state="disabled")

		cancel_file_butt = tk.Button(bottom_buttons_frame, font=email_page_font, text="Cancel File", bg=buttons_bg, command=cancel_file)
		cancel_file_butt.grid(column=8, row=10, padx=butt_padx, pady=butt_pady)

		def clear_entries():
			GlobalWidget.to_var.set("")
			from_var.set("")
			password_var.set("")
			subject_var.set("")
			cancel_file()
			to_entry.delete(0, "end")
			from_entry.delete(0, "end")
			password_entry.delete(0, "end")
			subject_entry.delete(0, "end")
			body_text.delete("1.0", "end-1c")

		clear_entries_butt = tk.Button(bottom_buttons_frame, font=email_page_font, text="Clear Entries", bg=buttons_bg, command=clear_entries)
		clear_entries_butt.grid(column=9, row=10, padx=butt_padx, pady=butt_pady)
			
		submit_butt = tk.Button(bottom_buttons_frame, font=email_page_font, text="Send", bg=buttons_bg, command=lambda:get_and_send(body_text))
		submit_butt.grid(column=10, row=10, padx=butt_padx, pady=butt_pady)

		email_frame.grid(column=10, row=10, padx=(10,10), pady=(20,4))
		# ~~~~~ENDFRAME~~~~~

class RecipientsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		recipient_var = tk.StringVar()

		page = SetFramesAndNavBar(self, "RecipientsPage", controller)

		recipient_frame = tk.LabelFrame(page.middle, font=frame_title_font, text="Recipient Options", bd=5, fg=frame_title_color)
		
		r_form_frame = tk.Frame(recipient_frame)
		r_form_frame.pack(padx=registry_padx, pady=registry_pady)

		recipient_label = tk.Label(r_form_frame, font=recipient_page_font1, text="Register Recipient:")
		recipient_label.grid(column=10, row=10)

		recipient_entry = tk.Entry(r_form_frame, textvariable =recipient_var, bg=entries_bg, font=recipient_page_font1)
		recipient_entry.grid(column=11, row=10, padx=(0, 2))

		def add_recipient():
			if recipient_var.get() == "":
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please enter the email address of someone to email later.")
			else:
				if recipient_var.get() not in registered_emails_listbox.get(0, "end"):
					recipient = NewRecipient(recipient_var.get())
					recipient.add_to_db()
					GlobalWidget.status_label.config(fg="green")
					GlobalWidget.status_label.config(text="'" + recipient_var.get() + "' has been added to Registered Emails.")
					update_registered_email_list_box()
				else:
					GlobalWidget.status_label.config(fg="red")
					GlobalWidget.status_label.config(text="Please do not enter duplicate email addresses; '" + recipient_var.get() + "' is already in Registered Emails.")

		register_butt = tk.Button(r_form_frame, font=recipient_page_font1, text="Register", bg=buttons_bg, command=add_recipient)
		register_butt.grid(column=12, row=10)

		registered_emails_frame = tk.Frame(recipient_frame)
		registered_emails_frame.pack(padx=registry_padx, pady=registry_pady)

		registered_emails_label = tk.Label(registered_emails_frame, font=recipient_page_font2, text="Registered Emails")
		registered_emails_label.grid(column=10, row=9, pady=(1,3))

		registered_emails_listbox = tk.Listbox(registered_emails_frame, width=30, height=12, font=recipient_page_font1)
		registered_emails_listbox.grid(column=10, row=10)

		#scrollbar
		y_scroll = tk.Scrollbar(registered_emails_frame, orient="vertical")
		registered_emails_listbox['yscrollcommand'] = y_scroll.set
		y_scroll['command'] = registered_emails_listbox.yview
		y_scroll.grid(column=10, row=10, sticky="nse")

		def update_registered_email_list_box():
			registered_emails_listbox.delete("0", "end")
			recipient_var.set("")
			recipient_object = OldRecipients()
			all_recipients = recipient_object.load_recipients()
			for recipient in all_recipients:
				registered_emails_listbox.insert("end", recipient)
		
		update_registered_email_list_box()

		registered_emails_butt_frame = tk.Frame(registered_emails_frame)
		registered_emails_butt_frame.grid(column=10, row=11, columnspan=2)

		def delete_registered_email():
			try:
				selected_email_address = registered_emails_listbox.get(registered_emails_listbox.curselection())
				selected = OldRecipients()
				selected.delete_recipient(selected_email_address)
				GlobalWidget.status_label.config(fg="green")
				GlobalWidget.status_label.config(text="'" + selected_email_address + "' has been deleted from Registered Emails.")
				update_registered_email_list_box()
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please click on an email address you would like to delete from Registered Emails.")

		delete_butt = tk.Button(registered_emails_butt_frame, font=recipient_page_font1, text="Delete", bg=buttons_bg, command=delete_registered_email)
		delete_butt.grid(column=10, row=10, padx=recipient_page_butt_padx, pady=recipient_page_butt_pady)

			

		def edit_registered_email():
			positionX = GlobalWidget.registered_edit_button_position[0]
			positionY = GlobalWidget.registered_edit_button_position[1]
			PADX = (5,5)
			PADY = (5,5)	
			try:
				def update_email(email_address):
					recipient = email_address
					updated_recipient = updated_email.get()
					selected = OldRecipients()
					selected.edit_recipient(recipient, updated_recipient)
					GlobalWidget.status_label.config(fg="green")
					GlobalWidget.status_label.config(text="'" + recipient + "' has been updated to '" + updated_recipient + "'")
					update_registered_email_list_box()
					window.destroy()

				updated_email = tk.StringVar()
				selected_email_address = selected_email_address = registered_emails_listbox.get(registered_emails_listbox.curselection())
				window = tk.Toplevel()
				window.geometry("+" + positionX + "+" + positionY)
				window.title("Edit Email Address")
				middle = tk.Frame(window)
				middle.pack()
				email_entry = tk.Entry(middle, textvariable=updated_email, font=edit_toplevel_font)
				email_entry.insert(0, selected_email_address)
				email_entry.grid(column=10, row=10, padx=PADX, pady=PADY)
				update_butt = tk.Button(middle, text="Update", command=lambda: update_email(selected_email_address))
				update_butt.grid(column=11, row=10, padx=PADX, pady=PADY)
				window.mainloop()
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please enter the email address that you would like to edit from Registered Emails.")
			

		edit_butt = tk.Button(registered_emails_butt_frame, font=recipient_page_font1, text="Edit", bg=buttons_bg, command=edit_registered_email)
		edit_butt.grid(column=11, row=10, padx=recipient_page_butt_padx, pady=recipient_page_butt_pady)
		#get the click event variables; x and y coordinates of where you clicked the dit button.
		edit_butt.bind("<1>", self.OnMouseDown)

		recipient_frame.grid(column=10, row=10, padx=(10,10), pady=(20,5))


	def OnMouseDown(self, event):
		#print("frame coordinates: %s/%s" % (event.x, event.y))
		#print("root coordinates: %s/%s" % (event.x_root, event.y_root))
		x = str(event.x_root - 100)
		y = str(event.y_root - 100)
		GlobalWidget.registered_edit_button_position = [x,y]


class ListsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		list_name_var = tk.StringVar()
		
		page = SetFramesAndNavBar(self, "ListsPage", controller)

		form_frame = tk.Frame(self)
		form_frame.pack()

		#Main Frame
		list_frame = tk.LabelFrame(page.middle, font=frame_title_font, text="Email Lists", bd=5, fg=frame_title_color)
		
		#Left Side of the Page
		create_list_frame = tk.Frame(list_frame)
		create_list_frame.pack(side="left", padx=side_frame_padx, pady=side_frame_pady)

		title_label_left = tk.Label(create_list_frame, font=lists_page_title_font, text="New List")
		title_label_left.grid(column=10, row=9, columnspan=2)

		name_label = tk.Label(create_list_frame, font=lists_page_font1, text="List Name:")
		name_label.grid(column=10, row=10, sticky="w")

		name_entry = tk.Entry(create_list_frame, textvariable=list_name_var, bg=entries_bg, font=lists_page_font1)
		name_entry.grid(column=11, row=10)

		def open_recipient_adder():
			positionX = GlobalWidget.add_recipients_butt_position[0]
			positionY = GlobalWidget.add_recipients_butt_position[1]
			def update_listbox():
				recipient_object = OldRecipients()
				all_recipients = recipient_object.load_recipients()
				for recipient in all_recipients:
					listbox.insert(0, recipient)
			def add_to_parent_listbox():
				do_nothing = False
				current_list_recipients = current_list_listbox.get(0, "end")
				for recipient in current_list_recipients:
					if listbox.get(listbox.curselection()) == recipient:
						do_nothing = True
				if do_nothing == False:
					try:
						current_list_listbox.insert("end", listbox.get(listbox.curselection()))
					except:
						pass
			def remove_from_parent_listbox():
				try:
					selected = listbox.get(listbox.curselection())
					current_list_recipients = current_list_listbox.get(0, "end")
					index_to_delete = None
					for recipient in enumerate(current_list_recipients):
						if recipient[1] == selected:
							index_to_delete = recipient[0]
					current_list_listbox.delete(index_to_delete)
				except:
					pass
			def close_recipient_adder():
				window.destroy()
		
			window = tk.Toplevel()
			window.geometry("260x210+" + positionX + "+" + positionY)
			window.title("Create List")
			left = tk.Frame(window)
			left.pack(side="top")
			right = tk.Frame(window)
			right.pack(side="right")
			bottom = tk.Frame(window)
			bottom.pack(side="bottom", pady=(5,10))

			listbox = tk.Listbox(left, width=30)
			listbox.grid(column=10, row=10)
			update_listbox()#runs once
			y_scroll3 = tk.Scrollbar(left, orient="vertical")
			listbox['yscrollcommand'] = y_scroll3.set
			y_scroll3['command'] = listbox.yview
			y_scroll3.grid(column=10, row=10, sticky="nse")

			add_butt = tk.Button(bottom, font=toplevel_butt_font, text="Add item", width=7, command=add_to_parent_listbox)
			add_butt.pack(side="left")
			
			done_butt = tk.Button(bottom, font=toplevel_butt_font, text="Done", width=7, command=close_recipient_adder)
			done_butt.pack(side="right")
			remove_butt = tk.Button(bottom, font=toplevel_butt_font, text="Remove", width=7, command=remove_from_parent_listbox)
			remove_butt.pack()

			window.mainloop()

		add_recipients_butt = tk.Button(create_list_frame, font=lists_page_butt_font, width=26, text="Edit/Add Recipients", bg=buttons_bg, command=open_recipient_adder)
		add_recipients_butt.grid(column=10, row=11, columnspan=2, pady=list_page_edit_butt_pady)
		add_recipients_butt.bind("<1>", self.OnMouseDown)

		current_list_label = tk.Label(create_list_frame, font=list_page_font2, text="Recipients On List")
		current_list_label.grid(column=10, row=12, columnspan=2)

		c_list_box_frame = tk.Frame(create_list_frame)
		c_list_box_frame.grid(column=10, row=13, columnspan=2)

		current_list_listbox = tk.Listbox(c_list_box_frame, font=lists_page_font1, height=12)
		current_list_listbox.grid(column=10, row=10)

		#scrollbar
		y_scroll1 = tk.Scrollbar(c_list_box_frame, orient="vertical")
		current_list_listbox['yscrollcommand'] = y_scroll1.set
		y_scroll1['command'] = current_list_listbox.yview
		y_scroll1.grid(column=10, row=10, sticky="nse")

		bottom_left_buttons_frame = tk.Frame(create_list_frame)
		bottom_left_buttons_frame.grid(column=10, row=14, columnspan=2)

		def save_current_list():
			seperator = "<[seperator]>"
			long_string_of_recipients = ""
			if current_list_listbox.get(0, "end") != () and list_name_var.get() != "":
				if list_name_var.get() not in all_lists_listbox.get(0, "end"):
					for recipient in enumerate(current_list_listbox.get(0, "end")):
						if recipient[0] != 0:
							long_string_of_recipients += seperator + recipient[1]
						else:
							long_string_of_recipients += recipient[1]
					new_list = NewList(list_name_var.get(), long_string_of_recipients)
					new_list.add_to_db()
					GlobalWidget.status_label.config(fg="green")
					GlobalWidget.status_label.config(text="New list '" + list_name_var.get() + "' has been created and added to My Lists.")
					update_all_lists_listbox()
				else:
					GlobalWidget.status_label.config(fg="red")
					GlobalWidget.status_label.config(text="Please enter a unique name for this list; '" + list_name_var.get() + "' is already in My Lists.")
			else:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please enter a name for your new list and select one or more email addresses to add to it.")

		def clear_entries():
			list_name_var.set("")
			current_list_listbox.delete(0, "end")
				

		clear_entrie_butt = tk.Button(bottom_left_buttons_frame, font= lists_page_butt_font, text="Clear Entries", bg=buttons_bg, command=clear_entries)
		clear_entrie_butt.grid(column=10, row=10, padx=list_page_b_buttons_padx, pady=list_page_b_buttons_pady)

		save_current_list_butt = tk.Button(bottom_left_buttons_frame, font= lists_page_butt_font, text="Save", bg=buttons_bg, command=save_current_list)
		save_current_list_butt.grid(column=11, row=10, padx=list_page_b_buttons_padx, pady=list_page_b_buttons_pady)


		#Right Side of the Page
		all_lists_frame = tk.Frame(list_frame)
		all_lists_frame.pack(side="right", padx=side_frame_padx, pady=side_frame_pady)

		title_label_right = tk.Label(all_lists_frame, font=lists_page_title_font, text="My Lists")
		title_label_right.grid(column=10, row=9)

		def update_all_lists_listbox():
			all_lists_listbox.delete(0, "end")
			list_object = OldLists()
			all_lists = list_object.load_list_names() 
			for LIST in all_lists:
				all_lists_listbox.insert("end", LIST[0])

		all_lists_listbox = tk.Listbox(all_lists_frame, font=lists_page_font1, height=17)
		all_lists_listbox.grid(column=10, row=10)

		update_all_lists_listbox()

		#scrollbar
		y_scroll2 = tk.Scrollbar(all_lists_frame, orient="vertical")
		all_lists_listbox['yscrollcommand'] = y_scroll2.set
		y_scroll2['command'] = all_lists_listbox.yview
		y_scroll2.grid(column=10, row=10, sticky="nse")

		bottom_right_buttons_frame = tk.Frame(all_lists_frame)
		bottom_right_buttons_frame.grid(column=10, row=11)

		def open_all_lists_editor():
			try:

				positionX = GlobalWidget.view_list_butt_position[0]
				positionY = GlobalWidget.view_list_butt_position[1]
				title = all_lists_listbox.get(all_lists_listbox.curselection())

				def update_selected_list_box():
					list_object = OldLists()
					long_string_of_email_addresses = list_object.load_this_list(title)
					long_string_of_email_addresses = long_string_of_email_addresses[0][0]
					list_of_email_addresses = long_string_of_email_addresses.split("<[seperator]>")
					selected_list_listbox.delete(0, "end")
					for email_address in list_of_email_addresses:
						selected_list_listbox.insert("end", email_address)

				
				def remove_email_address():
					try:
						selected = selected_list_listbox.get(selected_list_listbox.curselection())
						selected_list_recipients = selected_list_listbox.get(0, "end")
						index_to_delete = None
						for recipient in enumerate(selected_list_recipients):
							if recipient[1] == selected:
								index_to_delete = recipient[0]
						selected_list_listbox.delete(index_to_delete)
					except:
						pass


				def add_email_address():
					used_email_addresses = selected_list_listbox.get(0, "end")
					list_object = OldRecipients()
					all_email_addresses = list_object.load_recipients()
					unused_email_addresses = all_email_addresses

					for used_email_address in used_email_addresses:
						unused_email_addresses.remove(used_email_address)
					
					def update_unused_recipients_listbox(unused_email_addresses):
						for email_address in unused_email_addresses:
							unused_recipients_listbox.insert("end", email_address)
					def add_email_address_to_existing_list():
						try:
							selected = unused_recipients_listbox.get(unused_recipients_listbox.curselection())
							
							unused_recipients = unused_recipients_listbox.get(0, "end")
							index_to_delete = None
							for recipient in enumerate(unused_recipients):
								if recipient[1] == selected:
									index_to_delete = recipient[0]
							unused_recipients_listbox.delete(index_to_delete)
						
							recipients_in_this_list = list(selected_list_listbox.get(0, "end"))

							if selected not in recipients_in_this_list:
								recipients_in_this_list.insert(len(recipients_in_this_list), selected)
							else:
								selected_list_listbox.delete(0, "end")

							selected_list_listbox.delete(0, "end")	

							for recipient in recipients_in_this_list:
								selected_list_listbox.insert("end", recipient)
						except:
							pass
						
					def close_window():
						child_window.destroy()

					positionX = GlobalWidget.toplevel_child_coordinates[0]
					positionY = GlobalWidget.toplevel_child_coordinates[1]
					child_window = tk.Toplevel()
					child_window.title("Other Email Adresses")
					child_window.geometry("230x230+" + positionX + "+" + positionY)

					top = tk.Frame(child_window)
					top.pack(side="top")

					bottom = tk.Frame(child_window)
					bottom.pack(padx=(5,5), pady=(5,5))

					title_label = tk.Label(top, font=("", 12, "bold"), text="Other Email Addresses")
					title_label.grid(column=10, row=10)

					unused_recipients_listbox = tk.Listbox(top, width=30)
					unused_recipients_listbox.grid(column=10, row=11)

					update_unused_recipients_listbox(unused_email_addresses)


					#scrollbar
					y_scroll_child = tk.Scrollbar(top, orient="vertical")
					unused_recipients_listbox['yscrollcommand'] = y_scroll_child.set
					y_scroll_child['command'] = unused_recipients_listbox.yview
					y_scroll_child.grid(column=10, row=11, sticky="nse")

					add_butt = tk.Button(bottom, font=toplevel_butt_font, text="Add To List", command=add_email_address_to_existing_list)
					add_butt.grid(column=10, row=10)

					done_butt = tk.Button(bottom, font=toplevel_butt_font, text="Done", command=close_window)
					done_butt.grid(column=11, row=10)


					child_window.mainloop()
				

				def save_changes_made(name):
					seperator = "<[seperator]>"
					long_string_of_recipients = ""
					if selected_list_listbox.get(0, "end") != ():

						for recipient in enumerate(selected_list_listbox.get(0, "end")):
							if recipient[0] != 0:
								long_string_of_recipients += seperator + recipient[1]
							else:
								long_string_of_recipients += recipient[1]
						this_list = OldLists()
						this_list.edit_list(name, long_string_of_recipients)
						update_all_lists_listbox()
						window.destroy()
					else:
						pass
					

				window = tk.Toplevel(self)
				window.geometry("230x230+" + positionX + "+" + positionY)
				window.title("View or Edit List")
				top = tk.Frame(window)
				top.pack(side="top")

				bottom = tk.Frame(window)
				bottom.pack(padx=(5,5), pady=(5,5))
				
				title_label = tk.Label(top, font=("", 12, "bold"), text=title)
				title_label.grid(column=10, row=10)

				selected_list_listbox = tk.Listbox(top, width=30)
				selected_list_listbox.grid(column=10, row=11)

				update_selected_list_box()

				y_scroll4 = tk.Scrollbar(top, orient="vertical")
				selected_list_listbox['yscrollcommand'] = y_scroll4.set
				y_scroll1['command'] = selected_list_listbox.yview
				y_scroll4.grid(column=10, row=11, sticky="nse")


				remove_butt = tk.Button(bottom, font=toplevel_butt_font, text="Remove", command=remove_email_address)
				remove_butt.grid(column=10, row=10)

				add_butt = tk.Button(bottom, font=toplevel_butt_font, text="Add...",command=add_email_address)
				add_butt.grid(column=11, row=10)
				add_butt.bind("<1>", self.OnMouseDown_child_toplevel)

				save_butt = tk.Button(bottom, font=toplevel_butt_font, text="Save", command=lambda: save_changes_made(title))
				save_butt.grid(column=12, row=10)
				
				window.mainloop()
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select a list in order to view it.")

		def delete_selected_list():
			try:

				selected = all_lists_listbox.get(all_lists_listbox.curselection())
				selected_list = OldLists()
				selected_list.delete_list(selected)
				GlobalWidget.status_label.config(fg="green")
				GlobalWidget.status_label.config(text="'" + selected + "' has been deleted from My Lists.")
				update_all_lists_listbox()
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select a list in order to delete it.")
			
		def choose_selected_list():
			try:

				selected = all_lists_listbox.get(all_lists_listbox.curselection())
				controller.show_frame(StartPage)
				GlobalWidget.to_var.set("<[" + selected + "]>")
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select a list in order to send emails to it.")	

		all_lists_view_butt = tk.Button(bottom_right_buttons_frame, font=lists_page_butt_font, text="View", bg=buttons_bg, command=open_all_lists_editor)
		all_lists_view_butt.grid(column=10, row=10, padx=list_page_b_buttons_padx, pady=list_page_b_buttons_pady)
		all_lists_view_butt.bind("<1>", self.OnMouseDown)

		all_lists_delete_butt = tk.Button(bottom_right_buttons_frame, font=lists_page_butt_font, text="Delete", bg=buttons_bg, command=delete_selected_list)
		all_lists_delete_butt.grid(column=11, row=10, padx=list_page_b_buttons_padx, pady=list_page_b_buttons_pady)

		all_lists_choose_butt = tk.Button(bottom_right_buttons_frame, font=lists_page_butt_font, text="Choose", bg=buttons_bg, command=choose_selected_list)
		all_lists_choose_butt.grid(column=12, row=10, padx=list_page_b_buttons_padx, pady=list_page_b_buttons_pady)

		#Seperator Frame
		Seperator_frame = tk.Frame(list_frame, height=520, width = 10, bd=8, relief="sunken")
		Seperator_frame.pack(padx=seperator_padx, pady=seperator_pady)

		list_frame.grid(column=10, row=10, padx=(10,10), pady=(20,5))


	def OnMouseDown(self, event):
		#print("frame coordinates: %s/%s" % (event.x, event.y))
		#print("root coordinates: %s/%s" % (event.x_root, event.y_root))
		x = str(event.x_root - 200)
		y = str(event.y_root - 200)
		x2 = str(event.x_root - 60)
		y2 = str(event.y_root - 300)
		GlobalWidget.add_recipients_butt_position = [x,y]
		GlobalWidget.view_list_butt_position = [x2, y2]

	def OnMouseDown_child_toplevel(self, event):
		x = str(event.x_root - 170)
		y = str(event.y_root - 300)
		GlobalWidget.toplevel_child_coordinates = [x, y]


class AutofillPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		autofill_var = tk.StringVar()

		page = SetFramesAndNavBar(self, "AutofillPage", controller)

		autofill_frame = tk.LabelFrame(page.middle, font=frame_title_font, text="Autofill Options", bd=5, fg=frame_title_color)

		af_form_frame = tk.Frame(autofill_frame)
		af_form_frame.pack(padx=autofill_padx, pady=registry_pady)

		default_email_label1 = tk.Label(af_form_frame, font=recipient_page_font1, text="Default Autofill is: ")
		default_email_label1.grid(column=10, row=9, sticky="w")

		current_autofill_frame = tk.Frame(af_form_frame)
		current_autofill_frame.grid(column=11, row=9, columnspan=2, sticky="w")

		default_email_label2 = tk.Label(current_autofill_frame, font=autofill_font1, text=GlobalWidget.CURRENT_AUTOFILL, fg="Steel Blue")
		default_email_label2.grid(column=10, row=10, sticky="w")

		email_label = tk.Label(af_form_frame, font=recipient_page_font1, text="My Email Address:")
		email_label.grid(column=10, row=10)

		email_entry = tk.Entry(af_form_frame, textvariable=autofill_var, bg=entries_bg, font=recipient_page_font1)
		email_entry.grid(column=11, row=10, padx=(0, 2))

		def add_autofill():
			if autofill_var.get() == "":
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please enter an email address that belongs to you in order use it later.")
			else:
				if autofill_var.get() not in autofill_emails_listbox.get(0, "end"):
					GlobalWidget.status_label.config(fg="green")
					GlobalWidget.status_label.config(text="'" + autofill_var.get() + "' has been added to My Autofill.")
					autofill = NewAutofill(autofill_var.get())
					autofill.add_to_db()
					update_autofill_emails_list_box()
				else:
					GlobalWidget.status_label.config(fg="red")
					GlobalWidget.status_label.config(text="Please do not enter duplicate email addresses; '" + autofill_var.get() + "' is already in Registered Autofill.")

		add_butt = tk.Button(af_form_frame, font=recipient_page_font1, text="Register", bg=buttons_bg, command=add_autofill)
		add_butt.grid(column=12, row=10)

		autofill_emails_frame = tk.Frame(autofill_frame)
		autofill_emails_frame.pack(padx=registry_padx, pady=registry_pady)

		autofill_emails_label = tk.Label(autofill_emails_frame, font=recipient_page_font2, text="My Autofill")
		autofill_emails_label.grid(column=10, row=9, pady=(1,5))

		autofill_emails_listbox = tk.Listbox(autofill_emails_frame, width=30, height=10, font=recipient_page_font1)
		autofill_emails_listbox.grid(column=10, row=10)

		#scrollbar
		y_scroll = tk.Scrollbar(autofill_emails_frame, orient="vertical")
		autofill_emails_listbox['yscrollcommand'] = y_scroll.set
		y_scroll['command'] = autofill_emails_listbox.yview
		y_scroll.grid(column=10, row=10, sticky="nse")

		def update_autofill_emails_list_box():
			autofill_emails_listbox.delete("0", "end")
			autofill_var.set("")
			autofill_object = OldAutofill()
			all_recipients = autofill_object.load_autofill()
			for recipient in all_recipients:
				autofill_emails_listbox.insert("end", recipient)
		
		update_autofill_emails_list_box()

		autofill_emails_butt_frame = tk.Frame(autofill_emails_frame)
		autofill_emails_butt_frame.grid(column=10, row=11, pady=autofill_pady)

		def delete_registered_autofill():
			try:
				selected_autofill = autofill_emails_listbox.get(autofill_emails_listbox.curselection())
				selected = OldAutofill()
				selected.delete_autofill(selected_autofill)
				GlobalWidget.status_label.config(fg="green")
				GlobalWidget.status_label.config(text="'" + selected_autofill + "' has been deleted from My Autofill.")
				update_autofill_emails_list_box()
				if GlobalWidget.CURRENT_AUTOFILL == selected_autofill:
					GlobalWidget.CURRENT_AUTOFILL = "None"
					default_email_label2.config(text=GlobalWidget.CURRENT_AUTOFILL)
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select the email address you would like to delete.")

		delete_butt = tk.Button(autofill_emails_butt_frame, font=recipient_page_font1, text="Delete", bg=buttons_bg, command=delete_registered_autofill)
		delete_butt.grid(column=10, row=10, padx=recipient_page_butt_padx, pady=recipient_page_butt_pady)

		def edit_autofill_email():
			positionX = GlobalWidget.autofill_edit_button_position[0]
			positionY = GlobalWidget.autofill_edit_button_position[1]
			PADX = (5,5)
			PADY = (5,5)	
			try:
				def update_email(email_address):
					updated_email_address = updated_email.get()
					selected = OldAutofill()
					selected.edit_autofill(email_address, updated_email_address)
					if email_address == GlobalWidget.CURRENT_AUTOFILL:
						default_autofill = DefaultAutofill()
						default_autofill.edit_default_autofill(email_address, updated_email_address)
						GlobalWidget.CURRENT_AUTOFILL = updated_email_address
						default_email_label2.config(text=GlobalWidget.CURRENT_AUTOFILL)
					GlobalWidget.status_label.config(fg="green")
					GlobalWidget.status_label.config(text="'" + email_address + "' has been updated to " + "'" + updated_email.get() + "'.")
					update_autofill_emails_list_box()
					window.destroy()

				updated_email = tk.StringVar()
				selected_email_address = autofill_emails_listbox.get(autofill_emails_listbox.curselection())
				window = tk.Toplevel()
				window.title("Edit Email Address")
				window.geometry("+" + positionX + "+" + positionY)
				middle = tk.Frame(window)
				middle.pack()
				email_entry = tk.Entry(middle,textvariable=updated_email, font=edit_toplevel_font)
				email_entry.insert(0, selected_email_address)
				email_entry.grid(column=10, row=10, padx=PADX, pady=PADY)
				update_butt = tk.Button(middle, text="Update", command=lambda: update_email(selected_email_address))
				update_butt.grid(column=11, row=10, padx=PADX, pady=PADY)
				window.mainloop()
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select the email address you would like to edit.")

		edit_butt = tk.Button(autofill_emails_butt_frame, font=recipient_page_font1, text="Edit", bg=buttons_bg, command=edit_autofill_email)
		edit_butt.grid(column=11, row=10, padx=recipient_page_butt_padx, pady=recipient_page_butt_pady)
		edit_butt.bind("<1>", self.OnMouseDown)

		def set_default_email_address():
			try:
				selected_email_address = autofill_emails_listbox.get(autofill_emails_listbox.curselection())
				default_autofill = DefaultAutofill()
				default_autofill.set_new_autofill(selected_email_address)
				GlobalWidget.CURRENT_AUTOFILL = selected_email_address
				default_email_label2.config(text=GlobalWidget.CURRENT_AUTOFILL)
				GlobalWidget.status_label.config(fg="green")
				GlobalWidget.status_label.config(text="' " + GlobalWidget.CURRENT_AUTOFILL + "' is now your default email address for autofill purposes.")
			except:
				GlobalWidget.status_label.config(fg="red")
				GlobalWidget.status_label.config(text="Please select an email address to set as 'default' for autofill purposes.")

		makedefault_butt = tk.Button(autofill_emails_butt_frame, font=recipient_page_font1, text="Make Default", bg=buttons_bg, command=set_default_email_address)
		makedefault_butt.grid(column=12, row=10, padx=recipient_page_butt_padx, pady=recipient_page_butt_pady)

		autofill_frame.grid(column=10, row=10, padx=(10,10), pady=(20,5))

	def OnMouseDown(self, event):
		#print("frame coordinates: %s/%s" % (event.x, event.y))
		#print("root coordinates: %s/%s" % (event.x_root, event.y_root))
		x = str(event.x_root - 100)
		y = str(event.y_root - 100)
		GlobalWidget.autofill_edit_button_position = [x,y]

class PrewritePage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		page = SetFramesAndNavBar(self, "PrewritePage", controller)



app = EmailGUI()