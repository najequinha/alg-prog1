a, b, c = map(float, input().split())

if b > a and b > c:
    a, b = b, a
elif c > a and c > b:
    a, c = c, a
else:
    a = a

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
    
else:
    if (a**2) == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    elif (a**2) > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2) < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    
    if a == b and b == c:
        print("TRIANGULO EQUILATERO") 
    elif a == b and a != c or a == b and b != c or c == b and a != c or c == b and b != a or c == a and a != b or c == a and b != c:
        print("TRIANGULO ISOSCELES")

