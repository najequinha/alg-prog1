h1, h2 = map(int, input().split())

if h1 == h2:
    horas = 24
    print(f"O JOGO DUROU {horas} HORA(S)")

elif h2 < h1:
    horas = 24 - h1 + h2
    print(f"O JOGO DUROU {horas} HORA(S)")

else:
<<<<<<< Updated upstream:problemas260323/01_2303.py
horas = h2 - h1
=======
    horas = h2 - h1
>>>>>>> Stashed changes:problemas23_03/01_2303.py
    print(f"O JOGO DUROU {horas} HORA(S)")
