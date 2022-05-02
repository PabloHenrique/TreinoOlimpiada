linha1 = input().split(" ")

A, B, C = linha1

A = float(A)
B = float(B)
C = float(C)

at = (A * C) / 2
ac = 3.14159 * (C ** 2)
at2 = ((A + B) * C) / 2
aq = B ** 2
ar = A * B

print(f"TRIANGULO: {at:.3f}\nCIRCULO: {ac:.3f}\nTRAPEZIO: {at2:.3f}\nQUADRADO: {aq:.3f}\nRETANGULO: {ar:.3f}")