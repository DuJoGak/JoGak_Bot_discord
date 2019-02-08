import math
def so_in_su(n):
    word=""
    primes=[]
    d = 2
    m=n/2
    while d <= m:
        if n%d == 0:
            n = n/d
            primes.insert(0,int(d))
        else:
            d = d +1
    cnt = 2
    x = len(primes)
    flag = 0
    if x==0:
        return "소수입니다."
    while x>0:
        if primes.count(cnt)!=0:
            if flag==0:
                word+=str(str(cnt)+"^"+str(primes.count(cnt)))
                flag=1
            else:
                word+=str(" x"+str(cnt)+"^"+str(primes.count(cnt)))
            x-=primes.count(cnt)
        cnt+=1
    return word