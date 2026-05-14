def leitura():
    while True:
        try:
            frase = input()
            frase = list(frase)
            while len(frase) < 1 or len(frase) > 50:
                frase = frase(input())
            c_frase = verificacao(frase)
            print(c_frase)

        except EOFError:
            break
    
    
def verificacao(lista: list) -> str:
    italico = True
    negrito = True
    for i in range(len(lista)):
        if lista[i] == "_":
            if italico:
                lista[i] = "<i>"
                italico = False
            else:
                lista[i] = "</i>"
                italico = True
                
    for i in range(len(lista)):
        if lista[i] == "*":
            if negrito:
                lista[i] = "<b>"
                negrito = False
            else:
                lista[i] = "</b>"
                negrito = True
                
    return "".join(lista)

def main():
    leitura()

main()