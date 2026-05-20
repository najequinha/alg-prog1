def inverso(frase: list) -> list:
    inicial = 0
    final = len(frase) - 1
    while inicial < final:
        frase[inicial], frase[final] = frase[final], frase[inicial]
        inicial += 1
        final -= 1
    return frase

def apagarEspacos(frase: list) -> list:
    frase_s_e = []
    for i in range(len(frase)):
        if frase[i] != " ":
            frase_s_e.append(frase[i])
    return frase_s_e

def verificar(frase: list, invertida: list) -> bool:
    frase = apagarEspacos(frase)
    invertida = apagarEspacos(invertida) 
    palindromo = True
    for i in range(len(frase)):
        if frase[i] == invertida[i]:
            palindromo = True
        else:
            palindromo = False
            break
    return palindromo

def main():
    frase = input()
    frase_l = list(frase)
    invertida = inverso(list(frase))
    pal = verificar(frase_l, invertida)
    if pal:
        print("SIM")
    else:
        print("NAO")
    
    
main()