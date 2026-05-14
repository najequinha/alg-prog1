nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 6]

#----------------------------

def contagem(n: int) -> int:
    n = str(n)
    n = list(n)
    soma = 0
    for i in range(len(n)):
        inteiro = int(n[i])
        soma += nums[inteiro] 
    return soma

#----------------------------

def printarContagem(n: int):
    for i in range(n):
        j = int(input())
        leds = contagem(j)
        print(f"{leds} leds")

#----------------------------
        
def main():
    n = int(input())
    printarContagem(n)

#----------------------------

main()