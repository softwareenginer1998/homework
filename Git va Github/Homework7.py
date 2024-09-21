Matn = input("so'z kiritiing: ")
words = Matn.split()
for i in range(len(words)):
    if len(words[i]) % 2 != 0:
        words[i] = words[i][::-1]
Javob = ' '.join(words)
print(Javob)
