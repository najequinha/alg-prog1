def leitura():
    while True:
        try:
            frase = input()
            frase = sentenca(frase)
            print(frase)
     
        except EOFError:
            break

#----------------------------

def sentenca(frase: list) -> str:
    frase = list(frase)
    m = True
    for i in range(len(frase)):
        if frase[i] == " ":
            continue
        
        if m:
            if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
                m = False
                continue
            else:
                frase[i] = maiuscula(frase[i])
                m = False
        else:
            if ord(frase[i]) >= 97 and ord(frase[i]) <= 122:
                m = True
                continue
            else:
                frase[i] = minuscula(frase[i])
                m = True
    return "".join(frase)

#----------------------------

def maiuscula(t: str) -> str:
    t = chr(ord(t) - 32)
    return t

#----------------------------

def minuscula(t: str) -> str:
    t = chr(ord(t) + 32)
    return t

#----------------------------

def main():
    leitura()

#----------------------------

main()