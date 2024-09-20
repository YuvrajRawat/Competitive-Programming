def isPerfectNumber(a):
    sum = 1
    if a>1:
        for i in range(2, a):
            if a%i==0:
                sum += i
        if sum == a:
            return f"{a} is perfect number"
        else:
            return f"{a} is not perfect number"
    else:
        return f"{a} is not perfect number"
n = int(input("Enter a number : "))
result = isPerfectNumber(n)
print(result)
