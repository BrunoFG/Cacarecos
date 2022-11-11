n=(2**127)-1
q=n-1
k=0
while pow(int(q), 1, 2)==0:
    q/=2
    k+=1
print(pow(2, int(q)*4, n))