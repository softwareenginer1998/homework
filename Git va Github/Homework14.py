data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
data_with_float = []
for item in data:
    data_with_float.append((item[0], float(item[1])))
yangi_data = sorted(data_with_float, key=lambda x: x[1], reverse=True)
final_data = [(item[0], str(item[1])) for item in yangi_data]
print(final_data)