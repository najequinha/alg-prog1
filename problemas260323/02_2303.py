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
