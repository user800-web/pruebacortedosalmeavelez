import numpy as np
A = np.random.randint(11, size = (10, 10))
print(A)
filas = len(A)
columnas = len(A[0])
R = []
r = []
for i in range(0, len(A)):
    for j in range(0, len(A)):

