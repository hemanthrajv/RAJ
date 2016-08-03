a=int(input("Enter the num of elements:"))
x=[[int(input())] for i in range(a)]
for i in range(a):
    y=x[i][0]
    while y>=10:
        y=int(y/10)
    x[i].insert(0,y)
x=sorted(x)
for i in range(len(x)):
    print(x[len(x)-1-i][1],end='')
