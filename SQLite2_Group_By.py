import sqlite3
connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select city , count(*) from customers 
                            group by city having count(*) > 1
                            order by count(*) desc""")
#Veri tabanındaki birden fazla olan şehirleri Z-A ya ve fazladan aza doğru sıraladık
for row in cursor:
    print("City: " + str(row[0]))
    print("Count= " + str(row[1]))
    print("***************")
