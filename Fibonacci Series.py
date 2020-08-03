print("Enter the limit ")
n = int(input(""))
t1 = 0
t2 = 1

for x in range(0,n):
    print(t1)
    newTerm=t1+t2
    t1=t2
    t2=newTerm
    x+=1