r = int(input())

por_100 = r // 100

r_100 = r % 100

por_50 = r_100 // 50

r_50 = r_100%50

por_20 = r_50 // 20

r_20 = r_50 % 20

por_10 = r_20 //10

r_10 = r_20 % 10

por_5 = r_10 // 5

r_5 = r_10 % 5

por_2 = r_5 // 2

r_2 = r_5 % 2

por_1 = r_2 // 1

r_1 = r_2 % 1

print(f"{r}\n{por_100} nota(s) de R$ 100,00\n{por_50} nota(s) de R$ 50,00\n{por_20} nota(s) de R$ 20,00\n{por_10} nota(s) de R$ 10,00\n{por_5} nota(s) de R$ 5,00\n{por_2} nota(s) de R$ 2,00\n{por_1} nota(s) de R$ 1,00")
