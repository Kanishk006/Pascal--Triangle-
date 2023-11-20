n = int(input())
k = 1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = "")
    for l in range(0,i):
        if l==0 or i==0:
            k=1 
        else:
            k = k*(i - l)//l 
        print(k,end = " ")
    print()