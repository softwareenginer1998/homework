n = int(input("n ni kiriting: "))
sum = 0
if n > 0:
    result = []
    for i in range(1, n + 1):
        raqam = int('2' * i)
        result.append(str(raqam))
        sum += raqam
    print('+'.join(result) + f'={sum}')
