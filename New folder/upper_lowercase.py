def case(alpha):
    new_alpha = alpha[0].upper() + alpha[1:3] +alpha[3].upper() + alpha[4:] 
    return new_alpha

alphabet = "macdonald"
result = case(alphabet)
print(result)

