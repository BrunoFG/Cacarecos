from math import factorial


def primoFermat(p):
    if ((2**(p-1))-1)%p == 0:
    #if pow(2, p-1, p) == 1:
        return p
    return 0

def primoWilson(p):
    if factorial(p-1)%p==-1:
        return 1
    return 0
        
def primoForcaBruta(p):
    for i in range(2,p):
        if p%i==0:
            return 0
    return 1

for i in range(3, 10**3):
    x = primoFermat(i)
    y = primoForcaBruta(i)
    if x and (not y):
        print(x)
