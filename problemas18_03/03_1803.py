#CORRGIR 
a, b, c = map(int, input().split())
if a > b and b > c:
    print(f"{c}\n{b}\n{a}")
    
elif a > b and b < c:
    print(f"{b}\n{c}\n{a}")
    
elif b > a and a > c:
    print(f"{c}\n{a}\n{b}")
    
elif b > a and a < c:
    print(f"{a}\n{c}\n{b}")

elif c > a and a > b:
    print(f"{b}\n{a}\n{c}")

elif c > b and b > a:
    print(f"{a}\n{b}\n{c}")
    
print(f"\n{a}\n{b}\n{c}")
