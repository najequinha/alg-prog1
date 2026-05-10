def criarLista():
    l = [0] * 20
    for i in range(len(l)):
        n = int(input())
        l[i] = n
    return l

#----------------------------

def trocarPos(lista: list):
    inicial = 0
    final = 19
    while inicial <=9:
        lista[inicial], lista[final] = lista[final], lista[inicial]
        inicial +=1
        final-= 1
    return lista

#----------------------------

def main():
    listinha = criarLista()
    trocada = trocarPos(listinha)
    for i in range(len(trocada)):
        print(f"N[{i}] = {trocada[i]}")
        
#----------------------------
        
main()