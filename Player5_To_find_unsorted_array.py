a=int(input())
b=[int(input()) for i in range(a)]
c=b
c=sorted(c)
for x in range(a):
        if b[x]==c[x]:
                break
        else:
                print("Unsorted array")
