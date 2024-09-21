lst = [1, 2, 33, 5, 6, 7, 7]
target_number = int(input("Son kiriting: "))
pair_nums = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if target_number == lst[i] + lst[j]:
            pair_nums.append((i, j))
if pair_nums:
    for p in pair_nums:
        print(f"lst[{p[0]}] + lst[{p[1]}] = {target_number} (yig'indi: {lst[p[0]]} + {lst[p[1]]})")

