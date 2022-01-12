
ncase=int(input())


def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    

for case in range(ncase):
    n=int(input())
    
    prime=[-1]*n
    
    k=0
    for i in range(2,n):
        if isprime(i):
            prime[k]=i
            k+=1
            
    for i in range(k):
        for j in range(k):
            if prime[i]*prime[j]>n:
                break
            else:
                print(prime[i],prime[j],end=" ")
        
    print()
