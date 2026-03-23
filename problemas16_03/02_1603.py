n1, n2, n3 = map(float, input().split())
media = (n1+n2+n3)/3

print(f"Media: {media:.1f}")

if media>=6:
	print("Aprovado.")
elif media < 3:
	print("Reprovado.")
else:
	print("Exame.")
