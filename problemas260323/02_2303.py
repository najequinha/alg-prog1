<<<<<<< Updated upstream:problemas260323/02_2303.py
#se um maior que o outro: subtrai e divide
#se igual = 24

h_i, m_i, h_f, m_f = map(int, input().split())
tempo_i = h_i * 60 + m_i
tempo_f = h_f * 60 + m_f

if tempo_i == tempo_f:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif tempo_i < tempo_f:
    tempo = tempo_f - tempo_i
    horas = tempo // 60
    minutos = tempo % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
else:
    tempo = 24*60 - tempo_i + tempo_f
    horas = tempo // 60
    minutos = tempo % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
=======
h_i, m_i, h_f, m_f = map(int, input().split())

if h_i == h_f and m_i == m_f:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if h_f < h_i:
        horas = h_f - 24 + hi
        if m_f < m_i:
            minutos = 60 - m_i - m_f
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        elif m_f > m_i:
            minutos = m_f - m_i
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        else:
            minutos = 0
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        #60 - minutos + minutos
    else:
        horas = h_f - h_i
        if m_f < m_i:
            minutos = 60 - m_i - m_f
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        elif m_f > m_i:
            minutos = m_f - m_i
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        else:
            minutos = 0
            print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
>>>>>>> Stashed changes:problemas23_03/02_2303.py
