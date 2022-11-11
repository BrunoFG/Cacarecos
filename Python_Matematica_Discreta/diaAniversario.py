respostas = []
for a in range(5):
    for i in range(1, 32):
        if i%(2**(a+1))>=2**a:
            print(i, end=' ')
    respostas.append(int(input("\nO dia do seu aniversário está aqui? (1 para sim e 0 para não)\n")))
m=0
for i in range(len(respostas)):
    m+=respostas[i]*(2**i)
print(f'O dia do seu aniversário é {m}')
while True:
    a=True