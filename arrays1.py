A1=[11,22,33,44,55]
A2=[66,77,88,99,100]
A3=[]

i=0

for i in range(5):
    if i %2==0:
        A3.append(A1[i])
    elif i%2==1:
        A3.append(A2[i])
print(A3)           
