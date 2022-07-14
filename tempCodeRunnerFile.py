import pyodbc
def create_table_again():
	# Create a database or connect to one that exists
	conn = pyodbc.connect('Driver=ODBC DRIVER 17 FOR SQL SERVER;'
                  'Server=Atri\SQLEXPRESS;'
                  'Database=crm;'
                  'Trusted_Connection=yes;')


	# Create a cursor instance
	c = conn.cursor()

	# Create Table
	c.execute("""CREATE TABLE crm.dbo.crmt (
		first_name text,
		last_name text,
		id integer,
		address text,
		city text,
		state text,
		zipcode text)
		""")
	
	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()

create_table_again()