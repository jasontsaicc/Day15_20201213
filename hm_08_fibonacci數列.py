# 表示生成斐波那契數列的個數
def fibonacci(num):
    #初始化前兩個值
    a = 0
    b = 1

    # 記錄每次生成個數的索引
    current_index = 0
    # 循環判斷條件是否成立
    while current_index < num:
        result = a
        # 條件成立交換兩個變量的值
        a, b = b, a + b
        #
        current_index += 1
        yield result

# 創建生成器
f = fibonacci(500)

for value in f:
    print(value)