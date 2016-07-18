a=int(input())
status=0
for i in range(2,a):
    if(a%i==0):
        status=1
if status!=0:
    print("Not prime")
else:
    print("Prime")
