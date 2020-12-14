import copy
#淺拷貝：只會對可變類型的第一層對象進行拷貝，不會對子對象進行拷貝
# 拷貝成功後會開闢一個新的內存空間，存放拷貝的對象

# 不可變類型： 數字，字符串，元組

num1 = 1
# copy() 表是一個淺拷貝
num2 = copy.copy(num1)

# 查看後地址沒有發生變化，說明沒有對對象進行拷貝，也就說沒有開闢新的內存空間
print("num1:", id(num1), "num2:", id(num2))

# 對與不可變類型進行淺拷貝實際上，是對引用的一個拷貝，兩個變量值定的是同一個內存地址

# 元組淺拷貝
my_tuple1 = (3, 5)
my_tuple2 = copy.copy(my_tuple1)
print("my_tuple1:", id(my_tuple1), "my_tuple2", id(my_tuple2))

# 淺拷貝不會對不可變類型進行拷貝，也就說不會開闢內存內存空間，
# 對於不可變類型進行淺拷貝實際，是對引用的一個拷貝，兩個變量指定的是一個內存地址

# 可變類型： 列表，字典，集合
my_list1 = [1, 3, [4, 6]]

my_list2 = copy.copy(my_list1)

print("my_list1:", id(my_list1), "my_list2", id(my_list2))
print(my_list1)
print(my_list2)

my_list1.append(5)
print(my_list1, my_list2)

# 淺拷貝不會對子對象進行拷貝
print("my_list1[2]:", id(my_list1[2]), "my_list2[2]", id(my_list2[2]))
my_list1[2].append(3)
print(my_list1)
print(my_list2)