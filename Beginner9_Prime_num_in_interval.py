a,b=int(input()),int(input())
for j in range(a,b):
    for i in range(2,j):
        if(j%i==0):
            break
    else:
        print(j)
