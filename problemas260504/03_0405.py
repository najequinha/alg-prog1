def leitura():
    frase = input()
    frase = list(frase)
    lista_alf = contagem(frase)
    printar(lista_alf)

def contagem(frase: list) -> list:
    alf = [0] * 26
    cont_A = 0
    cont_a = 0
    for i in range(ord("A"), (ord("Z")+1)):
        for j in range(len(frase)):
            if ord(frase[j]) == i:
                alf[cont_A] += 1
        cont_A += 1
    for i in range(ord("a"), (ord("z")+1)):
        for j in range(len(frase)):
            if ord(frase[j]) == i:
                alf[cont_a] += 1
        cont_a += 1
    
    return alf

def printar(lista: list) -> None:
    ord_inicial = ord("A")
    for i in range(len(lista)):
        if lista[i] == 0:
            ord_inicial += 1
            continue
        else:
            print(f"{chr(ord_inicial)}: {lista[i]}")
            ord_inicial += 1

def main():
    leitura()

main()