try:
 n=int(input())
 if n<0:
  print("Negative")
 elif n>0:
  print("Positive")
 else:
  print("Zero")
except:
 print('invalid')
