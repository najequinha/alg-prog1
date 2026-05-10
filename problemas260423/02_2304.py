def criarLista(n: int):
    lista = [0] * 10
    lista[0] = n
    return lista

#----------------------------

def listaDobrada(lista: list):
    for i in range(1, len(lista)):
        lista[i] = lista[i-1] * 2
    return lista

#----------------------------
    
def main():
    n = int(input())
    listinha = criarLista(n)
    listadobrada = listaDobrada(listinha)
    for i in range(len(listadobrada)):
        print(f"N[{i}] = {listadobrada[i]}")
        
#----------------------------
    
main()