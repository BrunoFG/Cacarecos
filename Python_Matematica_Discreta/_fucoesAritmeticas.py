#   Teorema de Euler
#       - Função Totient ou Phi(x)

#   Função em Teoria dos Números (Função Aritmética)
#       F(): Naturais --> Reais

#   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#   Tal (n) = {quantidade de divisores de n}
#   Sigma (n) = {soma dos divisores de n}

# Ex: Tal (12) = ?
#       D = {1,2,3,4,6,12}
#       |D| (ordem de D) = 6 = Tal (12)

#   A função aritmética f() é multiplicativa se, MDC(m,n)=1, f(m.n) = f(m).f(n).

#   Teorama: Se f() é multiplicativa e F(n) = Sum(f(d) tal que, d|n), então F também é multiplicativa
#   Prova: supor que f() é multiplicativa e aplicar a definição.

#   Sigma(p^k) = k+1

#   Função Aritmética de Mobius
#         = 1, se n=1
#   mi(n) = 0, se E p²|n
#         = (-1)^r, se n=p1.p2...pr

def mi(n):
    if n==1:
        return 1
    for i in range(2,n+1):
        if n%(i**2)==0:
            return 0
    r=0
    for i in range(2,n):
        if n%i==0:
            r+=1
    if r==0:
        return -1
    return (-1)**r

while(1):
    print(mi(int(input())),end="\n\n")

n=10**6
div=0
for i in range(1,n+1):
    if n%i==0:
        div+=1
#print(div)