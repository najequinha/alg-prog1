#CORRGIR 
a, b, c = map(int, input().split())
if a > b and a > c:
    if b > c:
        print(f"{c}\n{b}\n{a}")
        print("")
        print(a, b, c)
    else:
        print(f"{b}\n{c}\n{a}")
        print("")
        print(a, b, c)
    
elif b > a and b > c:
    if a > c:
        print(f"{c}\n{a}\n{b}")
        print("")
        print(a, b, c)
    else:
        print(f"{a}\n{c}\n{b}")
        print("")
        print(a, b, c)
    
elif c > a and c > b:
    if a > b:
        print(f"{b}\n{a}\n{c}")
        print("")
        print(a, b, c)        
    else:
        print(f"{a}\n{b}\n{c}")
        print("")
        print(a, b, c)
       
#print(f"\n{a}\n{b}\n{c}")
