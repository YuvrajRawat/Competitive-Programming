# num = (int(input("Number : ")))
# rev = 0
# temp = num
# while temp!=0:
#     rem = temp%10
#     rev = rev *10 +rem
#     temp = temp//10
    
# if (rev==num):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# num = int(input())
# rev = 0
# temp = num

# while temp != 0:
#     rem = temp % 10 
#     rev = rev * 10 + rem
#     temp = temp // 10

# if rev == num:
#     print("palindrome")
# else:
#     print("not")

# num = int(input())
# rev = 0
# temp = num

# while temp!=0:
#     rem = temp % 10
#     rev = rev *10 + rem
#     temp = temp // 10

# if rev == num:
#     print("palindrome")
# else:
#     print("Not")

num = int(input())
rev = 0
temp = num

while temp!=0:
    rem = temp%10
    rev = rev*10 + rem
    temp = temp//10

if rev == num:
    print("yes")
else:
    print("not")