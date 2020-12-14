import copy
#深拷貝：只要發現對像有可變類型，那麼就是對該對象到最後一個可變類型的每一層對象進行拷貝
# 拷貝成功後會開闢新的內存地址

# 不可變類型： 數字，字符串，元組

# 1.數字
num1 = 1
num2 = copy.deepcopy(num1)

print("num1:", id(num1), "num2:", id(num2))

# 2.字符串
str1 = "hello python"
str2 = copy.deepcopy(str1)
print("str1:", id(str1), "str2:", id(str2))

# 3.元組
my_tuple1 = (1, [1, 2])
my_tuple2 = copy.deepcopy(my_tuple1)

print("my_tuple1:", id(my_tuple1), "my_tuple2", id(my_tuple2))

print("my_tuple1[0]:", id(my_tuple1[0]), "my_tuple2[0]", id(my_tuple2[0]))
print("my_tuple1[1]:", id(my_tuple1[1]), "my_tuple2[1]", id(my_tuple2[1]))

my_tuple2[1].append(4)
print(my_tuple1, my_tuple2)
# 如果發現元組裡面有可變類型，會對元組進行拷貝和子元素列表進行拷貝，
# 拷貝後都會產生一個新的內存空間
# 但是不可變類型不會進行拷貝，因為不可變類型不允許在原有內存空間的基礎修改數據
# 所以拷貝沒有意義，因為每次修改數據內存地址都會發生變化

# 可變類型：列表，字典，結合，對應深拷貝來說也會進行拷貝如果發現子對象
# 也是可變類型也會進行拷貝，拷貝後會開闢新的內存空間
my_list1 = [1, [2, 3]]
my_list2 = copy.deepcopy(my_list1)
print("my_list1:", id(my_list1), "my_list2", id(my_list2))
print("my_list1[1]:", id(my_list1[1]), "my_list2[1]", id(my_list2[1]))

#無論是淺拷貝還是深拷貝都是針對的可變類型