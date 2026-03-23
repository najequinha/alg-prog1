a, b, c = map(int, input().split())

if a >= b and a >= c:
    if b >= c:
        print(f"{c}\n{b}\n{a}")
    else:
        print(f"{b}\n{c}\n{a}")
    
elif b >= a and b >= c:
    if a >= c:
        print(f"{c}\n{a}\n{b}")
    else:
        print(f"{a}\n{c}\n{b}")
    
elif c >= a and c >= b:
    if a >= b:
        print(f"{b}\n{a}\n{c}")        
    else:
        print(f"{a}\n{b}\n{c}")
       
print(f"\n{a}\n{b}\n{c}")
