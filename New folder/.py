def find_pair_with_difference(arr, n, k):
    i, j = 0, 1

    while i < n and j < n:
        if i != j and arr[j] - arr[i] == k:
            return True
        elif arr[j] - arr[i] < k:
            j += 1
        else:
            i += 1

    return False

def main():
    t = int(input("Enter the number of test cases: "))
    
    results = []

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        result = find_pair_with_difference(arr, n, k)
        results.append(result)

    for result in results:
        if result:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
