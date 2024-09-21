n = int(input("son kirit: "))
sums = []
for i in range(1, n + 1):
    sequence = list(range(1, i + 1))
    current_sum = sum(sequence)
    formatted_sum = ''
    for num in sequence:
        formatted_sum += str(num) + '+'
    formatted_sum = formatted_sum[:-1] + '=' + str(current_sum)
    sums.append(formatted_sum)
for s in sums:
    print(s)