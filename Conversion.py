import numpy as np
A = np.random.randint(11, size = (10, 10))
print(A)
filas = len(A)
columnas = len(A[0])
R = []
r = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 1:
      r.append(A[i][j])
    cont = len(r)
R.append(cont)
print(R)
k = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 2:
      k.append(A[i][j])
    cont_dos = len(k)
R.append(cont_dos)
print(R)

