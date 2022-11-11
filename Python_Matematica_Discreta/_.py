# Se a tem ordem k (mod n), então a^h tem ordem k/MDC(k,h)
# Demo: Seja r a ordem de a^h e seja d = MDC(k,h)
# k = k1.d ; h = h1.d ; MDC(k1,h1)=1
# (a^h)^k1 = a^(h1.d.k/d) = a^(h1.k) = a^k^h1 cong 1^h1 cong 1 (mod n)
# (a^h)^k1 cong 1 (mod n) -> r|k1
# 

def mdc(a, b):
    if b>a:
        a, b = b, a
    if b==0:
        return a
    x = [1, 0]
    y = [0, 1]
    r = [b, b]
    print('\n a\tb\tr\tq\txn\tyn')
    while (r[1]!=0):
        q = a // b
        r[1] = a % b
        xn = x[0] - (q * x[1])
        yn = y[0] - (q * y[1])
        print('',a,'\t',b,'\t',r[1],'\t',q,'\t',xn,'\t',yn)
        x[0] = x[1]
        x[1] = xn
        y[0] = y[1]
        y[1] = yn
        a = b
        b = r[1]
        if (r[1]!=0):
            r[0] = r[1]
    return r[0], x[0], y[0]

def lincong(a,b,n):
    aOrig = a
    bOrig = b

    a = a % n
    b = b % n

    euclidesExtendido = mdc(a,n)
    d = euclidesExtendido[0]
    u = euclidesExtendido[2]
    # v = euclidesExtendido[2]

    # Nao tem solucao!
    if (b % d != 0):
        print('Nao existe solucao pra essa congruencia linear')
        return 0
    
    x0 = (u * (b/d)) % n

    if (x0 < 0):
        x0 += n

    resultados = []
    for i in range(0, d):
        an = (x0 + (i * (n/d))) % n
        resultados.append(an)
    
    print(aOrig, 'x =',bOrig,'(mod ' ,n,') | x: ',resultados)
    return resultados

lincong(11, 1, 81174)