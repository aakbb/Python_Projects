# Like : Veri tabanında herhangi bir data grubunda arama yapılmasını sağlar.
# Örneğin sadece isimlerinde 'a' bulunduran müşterileri görmek istediğinde like kullanırsın.

import sqlite3
connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select FirstName , LastName
                            from customers
                            where FirstName like '%a%'""")
#Yüzde işaretlerinin anlamı ilk yüzde: Başının ne olduğu önemli değil , ikinci yüzde: sonunun ne olduğu önemli değil.
for row in cursor:
    print("First Name: " + row[0])
    print("Last Name: " + row[1])
    print("****************")