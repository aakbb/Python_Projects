# Json da bir çeşit veri formatıdır.
#Genellikle tek tırnak ile koda başlanır
# Sebebi string ile karışmaması
# Devamında küme parantezi kullanılır.
#Küme parantezinin içinde string ifadeler ':'lar ve virgüller kullanılır 
# Bunlardan oluşan yapı bir json datasını oluşturur. Örneğin:
import json
data = '{"firstName" : "Ayse" , "lastName" : "AKBABA"}'
y= json.loads(data)
#9. Satırda String bir ifade olan data değişkenini json yapısına dönüştürmüş olduk
print(y["firstName"])
print(y["lastName"])
#SadeceString yapılar jsona çevrilmez.Dictionary i de biz json a çevirebilirz.
customer = {
    "firstName" : "Yasemen Nur",
    "e-mail" : "yakbaba252@gmail.com"
}
print(customer)
#dumps() python da türler arası dönüşüm yapılırken kullanılan birfornksiyondur.
customerJson = json.dumps(customer)
print(customer)
print(json.dumps("Yusuf"))