import tkinter as tk
import sqlite3

#Navbar Variables
navbar_button_font = ("", 16, "bold")
nav_button_fg = "Steel Blue"
border_color = "Steel Blue"

nav_butt_pady = (10,10)
nav_butt_padx = (30,0)


#Email Page Variables
email_page_font = ("", 20)
email_page_body_font = ("", 12)
email_page_path_font = ("", 14)
email_page_autofill_font = ("", 14, "bold")


#Recipient Page Variables
recipient_page_font1 = ("", 18)
recipient_page_font2 = ("", 25)
edit_toplevel_font = ("", 14)

registry_padx = (10,10)
registry_pady = (10,10)
recipient_page_butt_padx= (15,15)
recipient_page_butt_pady = (11,10)

#Lists Page Variables
lists_page_title_font = ("", 27)
lists_page_butt_font = ("", 12, "bold")
lists_page_font1 = ("", 14)
list_page_font2 = ("", 17)

list_page_edit_butt_pady = (8,14)
list_page_b_buttons_padx = (5,5)
list_page_b_buttons_pady = (5,5)

seperator_pady = (0,23)
seperator_padx = (6,6)
side_frame_padx = (10,10)
side_frame_pady = (15,25)


#Autofill Page Variables
autofill_font1 = ("", 15, "bold")
autofill_padx = (12,12)
autofill_pady = (0, 21)

#toplevel font
toplevel_butt_font = ("", 9, "bold")

#Other Variables... email page uses these too
frame_title_font = ("", 30)
frame_title_color = "Steel Blue"
buttons_bg = "powder blue"
entries_bg = "powder blue"

widget_pady = (5,5)
widget_padx = (20,20)
b_widget_padx = (20,20)
b_widget_pady = (10,10)
butt_padx= (5,20)
butt_pady= (0,10)
browse_padx = (20, 0)
browse_pady = (6, 20)
entry_width = 25
txt_width=42
txt_height=9


class GlobalWidget:
	registered_edit_button_position = None
	view_list_butt_position = None
	autofill_edit_button_position = None
	add_recipients_butt_position = None
	toplevel_child_coordinates = None
	to_var = None
	status_label = None

	try:
		conn = sqlite3.connect("emailManager.db")
		c = conn.cursor()
		c.execute("SELECT * FROM default_autofill")
		CURRENT_AUTOFILL = c.fetchall()[0][0]
		c.close()
		conn.close()
	except:
		CURRENT_AUTOFILL = "None"
	
	
	
	


	