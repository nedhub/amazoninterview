import collections
def addPolynomial(poly1, poly2):
    dic={}
    temp=poly1
    while temp!=None:
        dic[temp.power]=temp.coef
        temp=temp.next
    temp=poly2    
    while temp!=None:
        if temp.power in dic:
            dic[temp.power]+=temp.coef
        else:
            dic[temp.power]=temp.coef
        temp=temp.next
    
    od = collections.OrderedDict(sorted(dic.items(),reverse=True))
    lis=[]
    for k, v in od.items(): 
        lis.append("{}x^{}".format(v,k))
        lis.append(" + ")
        
    print("".join(lis[:-1]))    