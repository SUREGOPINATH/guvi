def common(arr,n):
  pre=arr[0]
  for i i range(1,n):
    pre=commonUtil(pre,arr[i])
  return(pre)
  
def commonUtil(s1,s2):
  res=""
  n1=len(s1)
  n2=len(s2)
  i=0
  j=0
  while i<=n1-1 and j<=n2-1:
    if(s1[i]!=s2[i]):
      break
    res+=s1[i]
    i+=1
    j+=1
  return(res)

n=int(input())
arr=[]
for i in range(n):
  s=input()
  arr.append(s)
res=common(arr,n)
print(res)
