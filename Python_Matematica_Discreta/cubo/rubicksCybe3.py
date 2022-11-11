def reverso(cubo, face, n):
    for i in range(n):
        for j in range(int(n/2)):
            cubo[face][i][j], cubo[face][i][-j-1] = cubo[face][i][-j-1], cubo[face][i][j]

def transposta(cubo, face, n):
    for i in range(n):
        for j in range(i+1, n):
            cubo[face][i][j], cubo[face][j][i] = cubo[face][j][i], cubo[face][i][j]
            
def move(cubo, n, face, orientation):
    if face == 0:
        faces = [1, 5, 3, 4]
    elif face == 1:
        faces = [2, 5, 0, 4]
    elif face == 2:
        faces = []
    elif face == 3:
        faces = [0, 5, 2, 4]
    elif face == 4:
        faces = [1, 0, 3, 2]
    elif face == 4:
        faces = [1, 2, 3, 0]
        
    if orientation=='h':
        transposta(cubo, face, n)
        reverso(cubo, face, n)

def F(cubo, n):
    #   Rotacionando os elementos da mesma face.
    transposta(cubo, 0, n)
    reverso(cubo, 0, n)
    
    #   Rotacionando os elementos adjacentes a face rotacionada.
    faces = [1, 4, 3, 5]
    for i in range(n):
        for f in range(3):
            cubo[faces[f]][-1][i], cubo[faces[f+1]][-1][i] = cubo[faces[f+1]][-1][i], cubo[faces[f]][-1][i]
            
def L(cubo, n):
    #   Rotacionando os elementos da mesma face.
    reverso(cubo, 4, n)
    transposta(cubo, 4, n)
    
    #   Rotacionando os elementos adjacentes a face rotacionada.
    for i in range(n):
        for f in range(3):
            cubo[3-f][i][0], cubo[2-f][i][0] = cubo[2-f][i][0], cubo[3-f][i][0]

def U(cubo, n):
    #   Rotação Horária na face superior
    transposta(cubo, 1, n)
    reverso(cubo, 1, n)
    
    #   Rotação nos elementos adjacentes da face
    for i in range(n):
        cubo[2][0][i], cubo[2][-1][-i-1] = cubo[2][-1][-i-1], cubo[2][0][i]
    
    faces = [0, 5, 2, 4]
    for i in range(n):
        for f in range(3):
            cubo[faces[f]][0][i], cubo[faces[f+1]][0][i] = cubo[faces[f+1]][0][i], cubo[faces[f]][0][i]
            
    for i in range(n):
        cubo[2][0][i], cubo[2][-1][-i-1] = cubo[2][-1][-i-1], cubo[2][0][i]

def originalPosition(cubo, n):
    cont = 0
    for face in range(6):
        for linha in range(n):
            for coluna in range(n):
                cont+=1
                if cubo[face][linha][coluna][0] != cont:
                    return False
    return True
                        
n = int(input("Digite a ordem N do cubo mágico. Ex: 2 (para um cubo 2x2x2)\n"))
cubo = [ [] for _ in range(6) ]
cont=1

#   Gerando o cubo a partir de um array multidimensional
for face in range(6):
    cubo[face] = [ [] for _ in range(n) ]
    for linha in range(n):
        cubo[face][linha] = [ [] for _ in range(n) ]
        
#   Enumerando as posições do cubo
for face in range(6):
    for linha in range(n):
        for coluna in range(n):
            cubo[face][linha][coluna].append(cont)
            cont+=1
            
#print(f'Faces:\nFrente: {cubo[0]}\nCima: {cubo[1]}\nTrás: {cubo[2]}\nBaixo: {cubo[3]}\nEsquerda: {cubo[4]}\nDireita: {cubo[5]}\n')
m=1
L(cubo, n)
U(cubo, n)
while (not originalPosition(cubo, n)):
    L(cubo, n)
    U(cubo, n)
    m+=1
print(f'Foram necessários {m} movimentos LU para o cubo voltar a posição original!')
F(cubo, n)
print(f'Faces:\nFrente: {cubo[0]}\nCima: {cubo[1]}\nTrás: {cubo[2]}\nBaixo: {cubo[3]}\nEsquerda: {cubo[4]}\nDireita: {cubo[5]}\n')

