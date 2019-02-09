import math

def is_prime(n):
    i=2
    while i<=math.sqrt(n):
        if int(n%i)==0:
            return False
        i+=1
    return True

def so_in_su(n):
    word=""
    primes=[]
    i=2
    if is_prime(n)==False:
        while n!=1:
            if n%i==0:
                primes.insert(0,i)
                n/=i
            else:
                i+=1
    else:
        print(n,", 소수입니다.")
        return 0
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