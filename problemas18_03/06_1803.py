a, b, c = map(float, input().split())

if a >= b and a >= c:
    if b >= c:
        #ordem: a, b, c
        a, b, c = a, b, c
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
            else:
                print("TRIANGULO ACUTANGULO")
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
    else:
        #ordem: a, c, b
        a, b, c = a, c, b
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

            else:
                print("TRIANGULO ACUTANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                


elif b >= a and b >= c:
    if a >= c:
        #ordem: b, a, c
        a, b, c = b, a, c
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

            else:
                print("TRIANGULO ACUTANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

    else:
        #ordem: b, c, a
        a, b, c = b, c, a
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

            else:
                print("TRIANGULO ACUTANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                


elif c >= a and c >= b:
    if a >= b:
        #ordem: c, a, b
        a, b, c = c, a, b
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

            else:
                print("TRIANGULO ACUTANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

    else:
        #ordem: c, b, a
        a, b, c = c, b, a
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
        else:
            if a ** 2 == (b**2+c**2):
                print("TRIANGULO RETANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                
            elif a ** 2 > (b**2+c**2):
                print("TRIANGULO OBTUSANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                

            else:
                print("TRIANGULO ACUTANGULO")
                
                if a == b and b == c:
                    print("TRIANGULO EQUILATERO") 
                else:
                    print("TRIANGULO ISOSCELES")
                    
else:
    print("vo trancar o curso")
                


