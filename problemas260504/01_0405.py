def leitura(n: int):
    for i in range(n):
        l = list(map(str, input().split()))
        str1, str2 = criarListas(l)
        palavra = combinar(str1, str2)
        print(palavra)
        
#----------------------------

def criarListas(lista: list):
    str1 = list(lista[0])
    str2 = list(lista[1])
    if len(str1) < len(str2):
        while len(str1) < len(str2):
            str1.append("")
    else: 
        while len(str2) < len(str1):
            str2.append("")
    return str1, str2
        
#----------------------------

def combinar(str1: list, str2: list) -> str:
    nova_str = []
    for i in range(len(str1)):
        nova_str.append(str1[i])
        nova_str.append(str2[i])
    return "".join(nova_str)

#----------------------------

def main():
    n = int(input())
    leitura(n)
        
#----------------------------

main()