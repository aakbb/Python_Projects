#Listelerin hata ayıklama yöntemi ile hesaplanması
#try-except yapısında kullanılan başka bir yapı da finally yapısıdır.
#Finally, ister try çalışsın ister except her türlü çalışacak metoddur.
#Bunu nerde kullanacağım peki?
#Mesela bir veri tabanı ile çalışırken yapılan her işlemden sonra dosyayı close() ile kapatmamız gerekiyordu.
#Yazdığımız kodda her seferinde close() yazmak yerine bir sefer finally e yazmamız kafi.
#Bu sayede sistemde hata da olsa sistem hem devam edecek hem de gereksiz açılmış olan dosyalar kapanacak.
import sys
liste = [7, "Ayşe" , 0 , 3 , "6"]

for i in liste:
    try:
        print("Sayı= " + str(i))
        sonuc = 1/int(i)
        print("Sonuç= " + str(sonuc))
    except ValueError:
        print("HATA: " +str(i) + " bir sayı değildir.")
    except ZeroDivisionError:
        print("HATA: Payda sıfır olamaz")
    except:
        print(str(i) + " hesaplanamadı.")
        print("Sistem hatası: " + str(sys.exc_info()[0]))
