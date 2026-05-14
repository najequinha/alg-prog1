def criarLista(n: int) -> list:
    l = list(map(int, input().split()))
    while len(l) != n:
        l = list(map(int, input().split()))
        
    return l

def menor(l: list):
    num = l[0]
    for i in range(len(l)):
        if l[i] <= num:
            num = l[i]
        ant = l[i]
    return num

def posicao(numero: int, l: list) -> list:
    l_pos = []
    for i in range(len(l)):
        if l[i] == numero:
            l_pos.append(i)
    return l_pos

def main():
    n = int(input())
    while n < 1 or n > 999:
        n = int(input())
    lista = criarLista(n)
    numero = menor(lista)
    pos = posicao(numero, lista)
    print(f"Menor valor: {numero}\nPosicao: {pos[0]}")
    
main()
    
