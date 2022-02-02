#Set Union :
# 'set1 | set2' ile ya da set1.union(set2) şeklinde gösterilir.
#Kümeler konusundaki A u B mantığıdır. Yani:
# s(A u B) = s(A) + s(B) - s(A-B)
#Setlerde de bu işlemi iki set arasında ortak olan terimleri sadece bir defa yazarak yeni bir set oluşturur.
#Örnek:
setA = {1,2,3,4,5,6}
setB = {2,4,6,8,6,5,9,0}
print(setA | setB)
print(setA.union(setB))