#Set Difference
#Kümelerdeki A - B (A kümesinin B kümesinden farkı / Fark Kümesi) 'dir.
# 'set1 - set2 ' ile ya da set1.difference(set2) gösterilir.
#Union ve intersection'de 1. ve 2. setlerin yerini değiştirdiğimizde sonuç değişmiyordu.
#Difference'de ise değişiyor.
#Örnek:
setA = {1,2,3,4,5,6}
setB = {2,4,6,8,6,5,9,0}

print(setA - setB)
print(setB - setA)
print(setA.difference(setB))
print(setB.difference(setA))