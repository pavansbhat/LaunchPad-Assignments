list_Trip=[1,1,2,3,4,64,35,93,35,87,4,3]
lis=[]
for x in list_Trip:
  if x not in lis:
    lis.append(x)
print(lis)
