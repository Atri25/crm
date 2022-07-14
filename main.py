import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
# import sqlite3
import pyodbc

# connect to database
# Some other example server values are
conn = pyodbc.connect('Driver=ODBC DRIVER 17 FOR SQL SERVER;'
                  'Server=Atri\SQLEXPRESS;'
                  'Database=studentmang;'
                  'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM studentmang.dbo.student')


def add():
    conn = pyodbc.connect('Driver=ODBC DRIVER 17 FOR SQL SERVER;'
                  'Server=Atri\SQLEXPRESS;'
                  'Database=studentmang;'
                  'Trusted_Connection=yes;')
        # Create cursor
    cursor = conn.cursor()
    # Insert into table
    cursor.execute(
        "INSERT INTO studentmang.dbo.student VALUES (? , ?, ?, ?, ? , ?, ?)",
        id.get(),
        name_strvar.get(),
        contact_strvar.get(),
        email_strvar.get(),
        gender_strvar.get(),
        stream_strvar.get(),
        dob.get()

)
    conn.commit()

def display_records():
    tree.delete(*tree.get_children())

    cursor.execute('SELECT * FROM studentmang.dbo.student')
    data = cursor.fetchall()

    for records in data:
        tree.insert('', END, values=records)

def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        cursor.execute('DELETE FROM studentmang WHERE id=%d' % int(selection[0]))
        cursor.commit()

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        display_records()

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")



# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

# Move Row Up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove Many records
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

# Clear entry boxes
def clear_entries():
	# Clear entry boxes
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	address_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)


# Select Record
def select_record(e):
	# Clear entry boxes
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	address_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	fn_entry.insert(0, values[0])
	ln_entry.insert(0, values[1])
	id_entry.insert(0, values[2])
	address_entry.insert(0, values[3])
	city_entry.insert(0, values[4])
	state_entry.insert(0, values[5])
	zipcode_entry.insert(0, values[6])

# Update record
def update_record():
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

	# Clear entry boxes
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	address_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)



# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

root.mainloop()