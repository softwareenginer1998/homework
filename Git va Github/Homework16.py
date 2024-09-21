list1 = eval(input("1-ro'yxatni kiriting (masalan, [1,2,3]): "))
list2 = eval(input("2-ro'yxatni kiriting: "))
list3 = eval(input("3-ro'yxatni kiriting: "))
list4 = eval(input("4-ro'yxatni kiriting: "))
all_lists = [list1, list2, list3, list4]
max_list = max(all_lists, key=sum)
print(max_list)