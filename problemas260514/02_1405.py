def minuscular(frase: list) -> list:
    lista_m = []
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            lista_m.append(chr(ord(frase[i]) + 32))
        else:
            lista_m.append(frase[i])

    return lista_m

#----------------------------

def separarPalavras(frase: list) -> list:
    palavras = []
    palavra = []
    
    for i in range(len(frase)):
        if frase[i] != " ":
            palavra.append(frase[i])
            
        else:
            palavras.append(palavra)
            palavra = []
            
    if palavra:
        palavras.append(palavra)
        
    return palavras

#----------------------------

def aliteracao(palavras: list) -> int:
    
    if len(palavras) < 2:
        return 0
    
    total_aliteracoes = 0
    em_aliteracao = False
    
    for i in range(1, len(palavras)):

        if palavras[i][0] == palavras[i-1][0]:
            if not em_aliteracao:
                total_aliteracoes += 1
                em_aliteracao = True
                
        else:
            em_aliteracao = False
        
    return total_aliteracoes
        
#----------------------------

def main():
    while True:
        try:
            frase = input()
            frase_m = minuscular(frase)
            palavras = separarPalavras(frase_m)
            res = aliteracao(palavras)
            print(res)
            
        except EOFError:
            break

#----------------------------

main()