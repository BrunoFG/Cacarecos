def decodificador(codigo):
    mensagem = []
    while codigo:
        num = codigo%27
        if not num:
            letra = chr(num+32)
        else:
            letra = chr(num+96)
        mensagem.append(letra)
        codigo = codigo // 27
    return "".join(mensagem)

n=int(input("Digite a mensagem codificada: "))
print(decodificador(n))
while True:
    a=True