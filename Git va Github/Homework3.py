list1 = ['Hello',123,True,'Goodbye','world',3.14,'7214']
Matn = sorted([item for item in list1 if isinstance(item, str)])
Teskari = sorted([item for item in list1 if item not in text], reverse=True)
print(Matn)
print(Teskari)