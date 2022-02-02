import sqlite3
def deleteCustomers():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""Delete from customers
                        where city = 'İstanbul' """)
    connection.commit()
    connection.close()

deleteCustomers()