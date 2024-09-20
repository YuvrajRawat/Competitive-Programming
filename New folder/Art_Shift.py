def art_shift(n, row):
  shifts = 0
  categories = ["H", "S", "P", "D"]

  for category in categories:
    category_positions = [i for i, art in enumerate(row) if art == category]

    for i in range(1, len(category_positions)):
      shifts += abs(category_positions[i] - (category_positions[0] + i))

  return shifts // 2

n = int(input())
row = input().split()

result = art_shift(n, row)
print(result)
