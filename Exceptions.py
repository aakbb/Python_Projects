#Exceptions: Kodlama sırasında karşılaşabileceğimiz hatalardır.
#Hata yaptığımızda ide bizi kırmızı yazıyla terminalde uyarır. 
#Ama bu uyarı anlaması biraz zordur.
#Bu yüzden kendi anlayacağımız şekilde uyarılar yazabiliriz.
#try - except komutlarını kullanacağız.
#Aynı anda try ve except çalışmaz. Ya try çalışır ya da except.

try:
    sayı = int(input("Sayı giriniz= "))

except ValueError:
    print("Tip uyuşmazlığı. Lütfen bir sayı giriniz.")

except :
    print("Bir hata oluştu.")