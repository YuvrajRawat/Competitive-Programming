num = int(input())

if num>0:
    fact = 1
    for i in range(1,num+1):
        fact*=i
    print("Yeh hai Fact :",fact)
else:
    print("Nhi hai Fact")
