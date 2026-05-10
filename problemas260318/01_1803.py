n1, n2, n3, n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print(f"Media: {media:.1f}")

if media >= 7:
	print("Aluno aprovado.")

elif media < 5:
	print("Aluno reprovado.")

elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    n_e = float(input())
    print(f"Nota do exame: {n_e:.1f}")
    n_media = (media + n_e)/2
    if n_media >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {n_media:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {n_media:.1f}")

