import numpy as np
num = float(input("Ingrese un numero: "))
entero = int(num)
decimal = num - entero
res = []
bin_ent = []
while entero > 0:
  bin_ent.append(str(entero % 2))
  entero = entero// 2
print("".join(bin_ent[::-1]))
if decimal == 0.0:
    res.append(0)
else:
    while decimal >= 0.01:
        decimal = decimal * 2
        if decimal >= 0 and decimal <= 0.999:
            bin = 0
            res.append(str(bin))
        else:
            bin_2 = 1
            res.append(str(bin_2))
        decimal = decimal - int(decimal)
    if decimal >= 0.0009:
        bin_3 = 0
        res.append(str(bin_3))
print(decimal)
res = ''.join(res)
print("Decimal a binario :p","".join(bin_ent[::-1]), ".", res)
