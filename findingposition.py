for i in range(int(input)):
    a=int(input())
    b=range(1,a+1)
    c=[]
    for j in b:
        c.append(j)
    while True:
        if len(c)==1:
            break
        else:
             c=c[1:len(c):2]
    d=b.index(c[0])
    print(d+1)