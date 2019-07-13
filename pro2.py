st,n=input().strip().split(" ")
n=int(n)
a=0
while a<len(st)-1 and n:
  if st[a]>st[a+1]:
    n-=1
    st=st[:a]+st[a+1:]
    if a!=0:
      a-=1
  else:
    a+=1
res=st[:len(st)-n]
print(res)
