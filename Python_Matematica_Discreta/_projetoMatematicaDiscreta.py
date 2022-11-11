# A) Codificador de Texto
from math import log2

def codificador(mensagem):
    mensagem = list(mensagem)
    m=0
    for i in range(len(mensagem)):
        asc = ord(mensagem[i])
        if asc!=32: 
            m += (asc-96)*(27**i)
    return m
    
def decodificador(codigo):
    mensagem = []
    while codigo:
        num = codigo%27
        if not num:
            letra = chr(num+32)
        else:
            letra = chr(num+96)
        print(f'resto: {num}, letra: {letra}')
        mensagem.append(letra)
        codigo = codigo // 27
    return "".join(mensagem)

def tam_por_bits(N):
    L = N/log2(27)
    return int(L)

mensagem = input("Mensagem: ")
resultado = codificador(mensagem)
N = len(bin(resultado)[2:])
print(f'N = {N} bits')
print(f'Tamanho da mensagem = {len(mensagem)}\nTamanho máximo da mensagem para que nenhuma\noutra exceda esta quatidade de bits {tam_por_bits(N)}')
print(f'Mensagem codificada: {resultado}')
print(decodificador(resultado))

