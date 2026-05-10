def leitura():
    l = [0] * 10
    for i in range(10):
        n = int(input())
        l[i] = n
    return l 

#-----------------------

def verificar(lista: list):
    for i in range(len(lista)):
        if lista[i] <= 0:
            lista[i] = 1
    return lista

#------------------------

def main():
    lista_nao_ver = leitura()
    lista_ver = verificar(lista_nao_ver)
    for i in range(len(lista_ver)):
        print(f"X[{i}] = {lista_ver[i]}")

main()