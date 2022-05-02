linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, num1, val1 = linha1
cod2, num2, val2 = linha2

cod1 = int(cod1)
num1 = int(num1)
val1 = float(val1)

cod2 = int(cod2)
num2 = int(num2)
val2 = float(val2)

total = (num1 * val1) + (num2 * val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")