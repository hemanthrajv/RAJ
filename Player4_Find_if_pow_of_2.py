def find_pow(x):
        while x>1:
                x=int(x**(1/2))
                if x==2:
                        print("The entered num is a power of 2")
                        break
find_pow(int(input()))
