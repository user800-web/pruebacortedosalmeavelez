import numpy as np
A = np.random.randint(1, 11, (10, 10))
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
k = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 2:
      k.append(A[i][j])
    cont_dos = len(k)
R.append(cont_dos)
l = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 3:
      l.append(A[i][j])
    cont_tres = len(l)
R.append(cont_tres)
m = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 4:
      m.append(A[i][j])
    cont_cuatro = len(m)
R.append(cont_cuatro)
n = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 5:
      n.append(A[i][j])
    cont_cinco = len(n)
R.append(cont_cinco)
o = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 6:
      o.append(A[i][j])
    cont_seis = len(o)
R.append(cont_seis)
p = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 7:
      p.append(A[i][j])
    cont_siete = len(p)
R.append(cont_siete)
q = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 8:
      q.append(A[i][j])
    cont_ocho = len(q)
R.append(cont_ocho)
k
r = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 9:
      r.append(A[i][j])
    cont_nueve = len(r)
R.append(cont_nueve)
s = []
for i in range(0, len(A)):
  acum = 0
  for j in range(0, len(A)):
    if A[i][j] == 10:
      s.append(A[i][j])
    cont_diez = len(s)
R.append(cont_diez)
print(R)

