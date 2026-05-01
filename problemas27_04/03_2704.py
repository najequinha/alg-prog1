def leitura():
    l = [0] * 100
    for i in range(len(l)):
        n = float(input())
        l[i] = n
    return l

#----------------------------

def listando(lista: list):
    for i in range(len(lista)):
        if lista[i] <= 10:
            print(f"A[{i}] = {lista[i]:.1f}")

#----------------------------

def main():
    lista_nums  = leitura()
    listando(lista_nums)
    
#----------------------------
        
main()