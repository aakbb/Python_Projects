import sqlite3
def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                        (firstName , lastName , city,email)
                        values ('Ayse' , 'AKBABA' , 'Sivas' , 'ayseakbb58@gmail.com')""")
    #yukarıdaki işlem veri tabanındaa bir tabloya veri eklemek için kullanılan kodlardır.
    connection.commit()
    #commit() fonksiyonu eklenen yeni verinin veri tablosuna işlenebilmesi için gerekli olan komuttur.
    connection.close()

insertCustomer()