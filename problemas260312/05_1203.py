a, b, c = map(float, input().split())
pi = 3.14159
a_tr = a*c/2
a_c = pi*c**2
a_tra = (a+b)*c/2
a_q = b**2
a_ret = a*b
print(f"TRIANGULO: {a_tr:.3f}\nCIRCULO: {a_c:.3f}\nTRAPEZIO: {a_tra:.3f}\nQUADRADO: {a_q:.3f}\nRETANGULO: {a_ret:.3f}")
