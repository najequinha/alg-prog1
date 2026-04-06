h1, h2 = map(int, input().split())

if h1 == h2:
    horas = 24
    print(f"O JOGO DUROU {horas} HORA(S)")

elif h2 < h1:
    horas = 24 - h1 + h2
    print(f"O JOGO DUROU {horas} HORA(S)")

else:
horas = h2 - h1
    print(f"O JOGO DUROU {horas} HORA(S)")
