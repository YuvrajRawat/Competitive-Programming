def CheckAnagram(word):
    digital_count = 0
    alphabet_count = 0

    for char in word:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            digital_count += 1
            
    summ = digital_count + alphabet_count
    return digital_count, alphabet_count, summ

n = "HISTORY1 23RAJa"
digital_count, alphabet_count, summ = CheckAnagram(n)
print(digital_count, alphabet_count, summ)

