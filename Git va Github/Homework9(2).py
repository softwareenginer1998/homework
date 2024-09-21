def tub_sonmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
son = int(input("Son kiriting: "))
count = 0
tub_sonlar = []

while count < 5:
    son += 1
    if tub_sonmi(son):
        tub_sonlar.append(son)
        count += 1
print(*tub_sonlar)