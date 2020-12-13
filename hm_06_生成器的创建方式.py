#根據程式師制定的規則迴圈生成數據，當條件不成立時則生成數據結束。
# 資料不是一次性全部生成處理，而是使用一個，再生成一個，可以節約大量的記憶體。

# 生成器的創建有兩種方式
# 1.生成器推導式，把列表推導式中的中括號改成小括號即可
# 2.yield 關鍵字 只要在函數里面看到有yield那麼這個函數可以任為是一個生成器

my_generator = (value *2 for value in range(3))
print(my_generator)

# # 生成器取值使用next函數獲取生成器中的下一個值
# value = next(my_generator)
# print(value)
# value = next(my_generator)
# print(value)
# value = next(my_generator)
# print(value)
# # 當生成器已經沒有值時，會拋出StopIteration，表示生成器生成數據完畢
# value = next(my_generator)
# print(value)

# while True:
#     try:
#         value = next(my_generator)
#         print(value)
#     except Exception as e:
#         break
#        跳出循環表示取值完成

# for:循環內部循環調用next函數獲取生成器中的下一值，
# 當出現異常for循環內部自動進行了異常捕獲。
for value in my_generator:
    print(value)
