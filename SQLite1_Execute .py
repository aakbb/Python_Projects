import sqlite3
connection = sqlite3.connect("chinook.db")
#Veri tabanı dosyasının adını yanlış yazarsan yanlış ada göre yeni bir veri tabanı dosyası oluşturur.
cursor = connection.execute("select * from customers")
cursor = connection.execute("select FirstName , LastName from customers")
# Cursor : Python da veri tabanında bir veriyi sorgulamak için kullanılan bir kelimedir.
# Select : Veri tabanından bana istediğğim datayı getir demek
# '*' : Veri tabanındaki verinin tüm kolonlarını getir demek
# From : Veri tabanındaki hangi tablodan veri çekeceksen tablo isminden önce from kullanırsın
#'*' yerine datadaki başlıkları yazarsak (line 5) first name index olarak 0 olurken last name 1 olacak 
#Yani benim 13 ve 14. satırlarda yazdığım indexler '*' yerine yazmış olduğum başlıkların indeksi.
for row in cursor:
    print("\n")
    print("First Name: " + row[0])
    print("Last Name: " + row[1])
    print("\n")
    print("*****************")
#String ifadeleri alt alta yazabilmek için üç tane çift tırnak ("") kullanılır.
cursor = connection.execute("""select FirstName , LastName 
                            from customers 
                            where city = 'Prague' or city = 'Berlin'
                            order by FirstName , LastName 
                            """)
#Line 21 de veri tabanındaki tüm verilerden şehiri Prague veya Berlin olanları bulup sadece onları yazmasını istedim
#Line 22 de isimleri alfabetik olarak sıralamasını istedim .
# A-Z sıralamak istediğimde FirstName den sonra asc yazmam lazımdı. 
#Ama asc yazmasak da otomatik olarak kendisi bunu yapıyor. Belirtip belirtmemek tamamen sizin tercihiniz.
#Tersten sıralamaki isteseydik de FirstName den sonra desc yazmamız gerekiyordu.
#Line 22 deki kullanımın anlamı A-Z ye verileri sırala
#Önce isimleri A-Z ye sırala. Aynı isimli kişilerin de soyadlarına göre A-Z ye sırala.
for row in cursor:
    print("\n")
    print("First Name: " + row[0])
    print("Last Name: " + row[1])
    print("\n")
    print("*****************")
# Line 19 da olduğu gibi sorular sorarak spesifik sorgulamalar da yapabiliriz