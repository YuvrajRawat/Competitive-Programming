def can_provide_change(num_cases, cases):
    result = []

    for case in cases:
        n = case[0]
        bills = case[1]

        change_5 = change_10 = 0

        for bill in bills:
            if bill == 5:
                change_5 += 1
            elif bill == 10:
                if change_5 > 0:
                    change_5 -= 1
                    change_10 += 1
                else:
                    result.append("NO")
                    break
            elif bill == 20:
                if change_10 > 0 and change_5 > 0:
                    change_10 -= 1
                    change_5 -= 1
                elif change_5 >= 3:
                    change_5 -= 3
                else:
                    result.append("NO")
                    break
        else:
            result.append("YES")

    return result
# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    bills = list(map(int, input().split()))
    test_cases.append((n, bills))

# Output
output = can_provide_change(t, test_cases)
for o in output:
    print(o)
