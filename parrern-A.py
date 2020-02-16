n=int(input("enter the number="))
for i in range(n):
  for j in range((n//2)+1):
    if ((j==0 or j==n//2) and i!=0) or (i==0 and j!=0 and j!=n//2) or (i==n//2):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
    