def derivada(coef: list) -> list:
    l = []
    for i in range(1, len(coef)):
        l.append(coef[i] * i)
                
    return l

def printar(l: list) -> None:
    for i in range(len(l)):
        print(f"{l[i]:.4f}")

def main():
    coef = list(map(float, input().split()))
    d = derivada(coef)
    printar(d)

main()