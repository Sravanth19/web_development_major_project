#fact=1
#n=int(input("enter number:"))
#for i in range (1,n+1):
#  fact=fact*i
#print(fact)  

#n=int(input("n:"))
#for i in range (1,11):
#  print(n,"*",i,"=",n*i)

n=int(input("number:"))
flag=False
if n==1:
  print("not prime")
elif n>1:
  for i in range(2,n):
    if (n%i)==0:
      flag=True
      break
  if flag:
    print("not prime")
  else :
    print("prime")