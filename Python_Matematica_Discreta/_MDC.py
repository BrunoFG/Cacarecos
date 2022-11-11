#   a | b
#   r   q
#   com 0 <= r < b

#   Dados a e b (inteiros), existem únicos q e r (inteiros) tais que a = qb + r com 0 <= r < b
#   X = {a - xb, x e Z, a e b dados, a - xb >= 0}
#   X é não vazio
#   X possui inteiros positivos

#   pelo Princípio da Boa Ordenância (PBO), X possui um menor elemento
#   Seja r0 o menor elemento de X
#   Supondo que r0 é >= b
#   Sabendo que r0 = a - x0.b
#   r1 = a - (x0 + 1).b --> r1 = r0 - b --> dado que r0 e b são positivos, r1 < r0 (absurdo! feriu o PBO)
#   portanto, 0 < r0 < b

#   a = q1.b + r1   0 <= r1 < b
#   a = q2.b + r2   0 <= r2 < b
#   q1 != q2        r1 != r2
#   prova por absurdo...

#   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#   MDC
#   teorema de euclides
#   livro numbers theory cap 2.2
#   lista de problemas 2.2 e 2.3

def MDC(a, b):
    if b>a:
        a, b = b, a
    if b==0:
        return a
    x = [1, 0]
    y = [0, 1]
    r = [b, b]
    print(f'\n a   | b   | r   | q   | xn  | yn')
    while (r[1]!=0):
        q = a // b
        r[1] = a % b
        xn = x[0] - (q * x[1])
        yn = y[0] - (q * y[1])
        print(f' {a}  | {b}  | {r[1]}  | {q}  | {xn}  | {yn}')
        x[0] = x[1]
        x[1] = xn
        y[0] = y[1]
        y[1] = yn
        a = b
        b = r[1]
        if (r[1]!=0):
            r[0] = r[1]
    return r[0]

while (1):
    n1 = int(input("Insira a: "))
    if n1 == 0: break
    n2 = int(input("Insira b: "))
    print(f'\nO MDC entre {n1} e {n2} é {MDC(n1, n2)}')
    print("")
    
# faz o MDC, se o MDC divide c, há solução
# xn.a + yn.b = MDC = d
# x0 = d.c, y0 = d.c
# x = x0 + (a/d).t
# y = y0 + (b/d).t