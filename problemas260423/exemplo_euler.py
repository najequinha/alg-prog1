def lerValores():
    x, n = map(int, input().split())
    while x < 1:
        x = int(input())
    while n < 0:
        n = int(input())
    return x, n

def fatorial(x: int):
    for i in range(x-1, 0, -1):
        x = x * i
    return x

def calculo(valor_x: int, parada_n: int):
    x = 1
    for i in range(1, parada_n+1):
        fat = fatorial(i)
        x += (valor_x ** i)/fat
    return x 

def main():
    x, n = lerValores()
    resultado = calculo(x, n)
    return resultado

resultado = main()

print(f"{resultado:.4f}")
