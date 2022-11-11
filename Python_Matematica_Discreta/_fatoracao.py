from cmath import sqrt
from math import ceil


n=1462771
for i in range(2,n):
    if n%i==0:
        print(i)
        
# Teorema de Wilson
# (n-1)! = -1 (mod n) se e somente se, n é primo
# (n-2)! = 1 (mod n) se e somente se, n é primo

# Teorema: x²+1 = 0 (mod p) tem solução se, somente se, p = 4k+1. Sendo p um número primo
# N = (m+d)(m-d)
def fatoracaoDeFermat(n):
    i = ceil(sqrt(n))
    d = 1.1
    for m in range(i, (n/2)+1):
        d = sqrt(m**2-n)
        if d-int(d)==0:
            break
