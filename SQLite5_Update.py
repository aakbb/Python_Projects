import sqlite3
def updateCustomers():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city ='İstanbul' 
                        where city = 'Sivas'""")
    connection.commit()
    connection.close()

updateCustomers()
