def criarLista():
    l = [0] * 10
    for i in range(10):
        n = int(input())
        l[i] = n
    return l

def parImpar(l: list):
    l_par = []
    l_impar = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            if len(l_par) == 5:
                for j in range(len(l_par)):
                    print(f"par[{j}] = {l[j]}")
                    l_par.clear
            else:
                l_par.append(l[i])
                
        else:
            if len(l_impar) == 5:
                for j in range(len(l_impar)):
                    print(f"impar[{j}] = {l[j]}")
                    l_impar.clear
            else:
                l_impar.append(l[i])
                
def main():
    lista = criarLista()
    parImpar(lista)
    
main()