def criarLista():
    l_par = []
    l_impar = []
    for i in range(15):
        n = int(input())
        if n % 2 == 0:
            l_par.append(n)
            if len(l_par) == 5:
                for j in range(len(l_par)):
                    print(f"par[{j}] = {l_par[j]}")
                l_par = []
            
        else:
            l_impar.append(n)
            if len(l_impar) == 5:
                for j in range(len(l_impar)):
                    print(f"impar[{j}] = {l_impar[j]}")
                l_impar = []
                
    for i in range(len(l_impar)):
        print(f"impar[{i}] = {l_impar[i]}")

    for i in range(len(l_par)):
        print(f"par[{i}] = {l_par[i]}")   
        
            

def main():
    criarLista()
    
main()
