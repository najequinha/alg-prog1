def main():
    while True:
        try:
            r_p = input()
            v  = int(input())
            res = leitura(r_p, v)
            print(res)
            
        except EOFError:
            break
            
def leitura(r_p: str, v: int) -> int:
    r_p = list(r_p)
    cont = 0
    l_r = []
    
    for i in range(len(r_p)):
        if r_p[i] == "W":
            cont += 1
            if len(l_r) >= 1:
                cont += 1
            l_r = []
            
        elif r_p[i] == "R":
            if len(l_r) == v:
                cont +=1
                l_r = []
            l_r.append(r_p[i])
            
    if l_r:
        cont += 1
        
    return cont

main()