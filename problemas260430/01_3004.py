def leitura(n: int):
    for i in range(n):
        frase = input()
        frase1 = primeiraP(frase)
        frase2 = segundaP(frase1)
        frase3 = terceiraP(frase2)
        frase = "".join(frase3)
        print(frase)

def primeiraP(frase: str) -> list:
    lista_frase = list(frase)
    for i in range(len(lista_frase)):
        if ord(lista_frase[i]) >= 65 and ord(lista_frase[i]) <= 90 or ord(lista_frase[i]) >= 97 and ord(lista_frase[i]) <= 122:
            lista_frase[i] = chr(ord(lista_frase[i]) + 3)
    return lista_frase

def segundaP(frase1: list) -> list:
    inicial = 0
    final = len(frase1) - 1
    while inicial < final:
        frase1[inicial], frase1[final] =  frase1[final], frase1[inicial]
        inicial += 1
        final -= 1
    return frase1

def terceiraP(frase2: list) -> list:
    m = (len(frase2) // 2)
    for i in range(m, len(frase2)):
        frase2[i] = chr(ord(frase2[i]) - 1)
    return frase2

def main():
    n = int(input())
    leitura(n)
    
main()