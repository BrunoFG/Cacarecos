import numpy as np

def L(face):
    for i in range (n-1):
        aux = face[0][0]
        face[0][0] = face[0][-1]
        face[0][-1] = face[-1][-1]
        face[-1][-1] = face[-1][0]
        face[-1][0] = aux        

n = 2#int(input())
cubo = [[],[],[],[],[],[]]
cont=1
for k in range(6):
    cubo[k] = np.zeros((n,n))
for k in range(6):
    for i in range(n):
        for j in range(n):
            cubo[k][i][j] = cont
            cont+=1
print(cubo)
L(cubo[4])
print(cubo)
