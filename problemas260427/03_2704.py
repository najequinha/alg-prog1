def criarLista(n: int):
    l = [0]
    l[0] = n
    return l 
    
#----------------------------

def preencherLista(n: int, l: list):
    x = n 
    for i in range(1, 30):
        x /= 2
        l.append(x)
    return l

#----------------------------

def printar(l: list):
    for i in range(len(l)):
        print(f"N[{i}] = {l[i]:.4f}")

#----------------------------
        
def main():
    n = float(input())
    lista = criarLista(n)
    lista_p = preencherLista(n, lista)
    printar(lista_p)

#----------------------------
    
main()