n=int(input())
ls=list(map(int,input().split()))
if len(ls)==n:
    a=[]
    res=""
    for i in range(len(ls)):
        x=ls[i]
        for j in range(len(ls)):
            if i!=j and ls[i]==ls[j]:
                a.append(ls[j])
    if len(a)!=0:
        a=set(a)
        for i in a:
            res+=str(i)
        print(res)
    else:
        print("unique")
    
