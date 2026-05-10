def criarLista(t: int):
    l = [0] * 30
    cont = 0
    for i in range(len(l)):
        if cont == t:
            cont = 0
        l[i] = cont
        cont += 1
    return l

#----------------------------

def main():
    t = int(input())
    lista = criarLista(t)
    for i in range(len(lista)):
        print(f"N[{i}] = {lista[i]}")
        
#----------------------------

main()