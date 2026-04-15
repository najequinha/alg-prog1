cap = float(input())
apo = float(input())
tax = float(input()) / 100
ano = int(input())

tempo = ano * 12
inicial = cap


for i in range(1, tempo+1):
    cap =  cap * (1 + tax)
    cap += apo


total = cap
t_apo = (apo * tempo) + inicial
rend = total - t_apo


print(f"Total em aportes: R$ {t_apo:.2f}")
print(f"Total em rendimentos: R$ {rend:.2f}")
print(f"Total final em conta: R$ {total:.2f}")