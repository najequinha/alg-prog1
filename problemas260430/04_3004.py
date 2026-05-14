def leitura(n: int):
    for i in range(n):
        frase = input()
        frase = list(frase)
        frase_ = criarListas(frase)
        print(frase_)
        
def criarListas(frase: list) -> str:
    metade = (len(frase) // 2) - 1
    esquerda = []
    direita = []
    for i in range(len(frase)):
        if i <= metade:
            esquerda.append(frase[i])
        else:
            direita.append(frase[i])
            
    esquerda = inverter(esquerda)
    direita = inverter(direita)
    
    return "".join(esquerda + direita)

def inverter(lista: list) -> list:
    inicial = 0
    final = len(lista) - 1
    while inicial < final:
        lista[inicial], lista[final] =  lista[final], lista[inicial]
        inicial += 1
        final -= 1
    return lista
    

def main():
    n = int(input())
    leitura(n)

main()