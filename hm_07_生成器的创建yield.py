# 在函數裡面看到有yield關鍵字，那麼這個函數就是生成器
def my_generator():
    for i in range(3):
        print("開始生成數據...")
        yield i
        print("上一次的數據生成好了...")

result = my_generator()
print(result)

# 獲取生成器下一個值
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)

# 生成器把所有數據生成完畢後，再次其它生成器會拋出一個StopIteration異常

for value in result:
    print (value)
