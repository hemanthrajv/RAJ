a=int(input())
b=int(0)
while a!=0:
        b=b*10
        b+=int(a%10)
        a=int(a/10)
print(b)
