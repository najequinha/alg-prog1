a, b, c = map(float, input().split())
if a == 0: 
	print("Impossivel calcular")
else:
	delta = b**2 - 4 * a * c
	if delta > 0 or delta == 0:
		r1 = ((-b) + (delta**0.5))  / (2 * a)
		r2 = ((-b) - (delta**0.5))  / (2 * a)
		print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
	else:
		print("Impossivel calcular")

