def leitura():
    valores = list(map(float, input().split()))
    casos = int(input())
    printar(casos, valores)


def calcular(valores: list, valor: float) -> float:
    cont = 0
    soma = 0
    for i in range(len(valores)):
        soma += (valores[i] * (valor ** cont))
        cont += 1
    return soma

def printar(casos: int, valores: list) -> None:
    for i in range(casos):
        n = float(input())
        res = calcular(valores, n)
        print(f"{res:.4f}")

def main():
    leitura()

main()