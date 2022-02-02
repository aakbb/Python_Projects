"""
geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. 

"""

print("""
     **********************************************
     Welcome to Find The Geometric Shape Program
     **********************************************
      """)

polygon = input("Type of the Polygon(Triangle or Quadrangle):")

if polygon == "Quadrangle":
    print("Enter the edges' length:")
    e1 = int(input("Edge1 = "))
    e2 = int(input("Edge2 = "))
    e3 = int(input("Edge3 = "))
    e4 = int(input("Edge4 = "))
    if e1==e2==e3==e4:
        print("This Shape's Name is = Square")
    elif (e1 == e2 and e3 ==e4) or (e1 ==e3 and e2 ==e4) or(e1 == e4 and e2==e3):
        print("Ths Shape's Name is = Rectangle")
    else:
        print("This Shape is not a special Quadrangle")
elif polygon == "Triangle":
    print("Enter the edges' length:")
    e1 = int(input("Edge1 = "))
    e2 = int(input("Edge2 = "))
    e3 = int(input("Edge3 = "))
    if abs(e1-e3) < e2 < (e1+e3) and abs(e1-e2) < e3 < (e1+e2) and abs(e2-e3) < e1 < (e2+e3): 
        if e1==e2==e3:
            print("This Shape's Name is = Equilateral Triangle")
        elif (e1==e2!=e3) or (e1==e3!=e2) or(e2==e3!=e1):
            print("This Shape's Name is = Isosceles Triangle")
        else:
            print("This Shape is not a Special Triangle")
    else:
        print("This Shape can not form a Triangle! Please Check the Edges' Length!")
else:
    print("Invalid Polygon Name! This Program Checking Only Triangle and Quadrangle")
    
