i = (int(input()))
anos = i//365

r_anos = i % 365

meses = r_anos // 30

dias = r_anos%30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")

