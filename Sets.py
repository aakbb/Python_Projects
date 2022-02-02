#Setler de tıpkı listeler gibi bir yapıya sahiptir.
#Küme parantezi '{}' ile gösterilir.
#Hızlı bir veri tipidir.
#Sette var olan bir datayı değiştiremezsin ama ekleme - çıkarma yapabilirsin.
#Setin tuple ve listelerden farkı ise iki tanedir
    #Sırasız ve indexsiz bir veri yapısıdır.Yazdırdığınız zaman sizin yazdığınız sıraya göre değil kendi
#yazılımındaki sıralamaya göre yazar.
    #İçinde bulunan elemanlar unique yani eşsizdir. Bir elemandan sadece bir tane bulunur.
        #Örnek: 
        # a = {1,2,3,(a,b,c) ,"Ayşe"}   //Doğru set yapısı
        # b = {1,1,2,3,(a,b,c) , "Ayşe"}    //Yanlış set yapısı(İçinde tekrar eden eleman var.)

students_Set = {"Ahmet" ,"Toprak" , "Derin" ,  "Sinan"}
print(students_Set)

#Set Fonksiyonu
#Sadece bir eleman alabilir. Elemanı harflerine ayırır.Tekrar eden ögelrei sadece bir defa yazar. 
#Harflerin yerleri yine sistemin kendinde belirlediği bir algoritmaya göre belirlenir.
students_Set2 = set("Abdulrezzak")
print(students_Set2)

for student in students_Set:
    print(student)

#In Keyword 
#Setlerde hangi elemanların olduğunu tüm elemanları yazdırmadan sorgulamak için kullanılır.
#in anahtar kelimesi setin içinde .... var mı? 'yı kontrol eder. Bunun sonucunda da true veya false dönderir.
print("derin" in students_Set)  #Python da büyük küçük harf duyarlıdır.
print("Derin" in students_Set)

#Add ve Remove Fonksiyonları
#Set'e yeni bir data eklemek için kullanılan bir fonksiyondur.
students_Set.add("Engin")
print(students_Set)
students_Set.remove("Ahmet")
print(students_Set)

#Update Fonksiyonu
#Set'e birden fazla data girişi sağlamak için kullanılan bir fonksiyondur.
students_Set.update(["Dila" , "Enes" , "Mert"])
print(students_Set)

#Len fonksiyonunu setlerde de kullanabiliyoruz
print(len(students_Set))

#Discard Fonksiyonu
#Bu da bir silme fonksiyonudur.
#Remove'den farkı eğer silinen bir ögeyi remove'da tekrar silmeye çalışırsan sistem hata verir.
#Discard'da ise kontrol ediyor. Eğer öge silinmemiş ise ögeyi siliyor.Silinmiş ise hata vermiyor.
students_Set.discard("Ahmet")
print(students_Set)

#Pop Fonksiyonu
#Kendi algoritmasına göre sıraladığı setten random bir elemanı siliyor.
#Setlerde fazla kullanılmayan bir fonksiyondur
x = students_Set.pop()
print(students_Set)

#Clear Fonksiyonu
#Tüm set'i siler ve ekrana boş bir set yazar. Eğer set'in tamamını silmek istiyorsan del anahtar kelimesini kullanırsın.
students_Set.clear()
print(students_Set)