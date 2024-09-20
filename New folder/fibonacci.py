# n_terms = int(input ("How many terms the user wants to print? "))  
  
# n_1 = 0  
# n_2 = 1  
# count = 0  
  
# if n_terms <= 0:  
#     print ("Not valid")  

# elif n_terms == 1:  
#     print(n_1)  

# else:  
#     print ("The fibonacci sequence of the numbers is:")  
#     while count < n_terms:  
#         print(n_1)  
#         nth = n_1 + n_2  
#        # At last, we will update values  
#         n_1 = n_2  
#         n_2 = nth  
#         count += 1 


def fibonacci(n_term):
    n1 = 0
    n2 = 1 
    count = 0
    fibo = []

    if n_term == 0:
        return "Invalid"
    elif n_term == 1:
        return [0]
    else:
        while count < n_term:
            fibo.append(n1)
            nth = n1 + n2
            
            n1 = n2
            n2 = nth
            count += 1
            
    return sum(fibo)



print(fibonacci(9))