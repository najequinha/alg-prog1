def tirarEspaco(frase: list) -> list:
    sem_espaco = []
    for i in range(len(frase)):
        if frase[i] != " ":
            sem_espaco.append(frase[i])
            
    return sem_espaco

def listarPalavras(l: list, pal: list) -> list:
    ps = []
    

    for i in range(len(l)):
        p = []
        
        if i == len(l) - (len(pal) - 1):
            break
        for j in range(i, i+len(pal)):
            p.append(l[j])
            
        pa = "".join(p)
        ps.append(pa)
        p = []

    return ps

def verificar(lista_pal : list, pal: list) -> bool:
    palavrinha = "".join(pal)
    cont = 0
    valor = False
    for i in range(len(lista_pal)):
        palavra = "".join(lista_pal[i])
        if palavra == palavrinha:
            cont += 1
            
        if cont >= 1:
            valor = True
                        
    return valor

def main():
    f = input()
    f = list(f)
    p = input()
    p = list(p)
    frase = tirarEspaco(f)
    lista = listarPalavras(frase, p)
    res = verificar(lista, p)
    if res:
        print("SIM")
    else:
        print("NAO")
        
main()
