def fibo(enesimo: int):
    if enesimo == 0:
        return 0
    
    elif enesimo == 1:
        return 1
    
    f1 = 0
    f2 = 1
    for i in range(2, enesimo+1):
        fn = f1 + f2
        f1, f2 = f2, fn
    
    return fn

#----------------------------

def casos(t: int):
    for i in range(t):
        n = int(input())
        n_fibo = fibo(n)
        print(f"Fib({n}) = {n_fibo}")

#----------------------------
        
def main():
    t = int(input())
    casos(t)

#----------------------------
    
main()
