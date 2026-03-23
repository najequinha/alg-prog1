t, add_q, b_r = map(str, input().split())
if t == "P":
   valor = 15
   #add_q = input()
   if add_q == "S":
       valor += 2.5
       #valor = 15 + 2.5
   else:
       valor = valor
   #b_r = input()
   if b_r == "S":
        valor += 5
        print(f"Total: R$ {valor:.2f}")
   else:
        valor = valor 
        print(f"Total: R$ {valor:.2f}")

elif t == "M":
   valor = 18.5
   #add_q = input()
   if add_q == "S":
       valor += 4
       #valor = 15 + 4
   else:
       valor = valor
   #b_r = input()
   if b_r == "S":
        valor += 5
        print(f"Total: R$ {valor:.2f}")
   else:
        valor = valor 
        print(f"Total: R$ {valor:.2f}")


else:
   valor = 23
   #add_q = input()
   if add_q == "S":
       valor += 4
       #valor = 15 + 4
   else:
       valor = valor
   #b_r = input()
   if b_r == "S":
        valor += 5
        print(f"Total: R$ {valor:.2f}")
   else:
        valor = valor 
        print(f"Total: R$ {valor:.2f}")





