# 為了確保檔案關閉 使用try except 但太長不好用
# try:
#     file = open("1.txt", "r")
#     result = file.write("HELLO PYTHON")
# except Exception as  e:
#     print(e)
# finally:
#     print("over")
#     file.close()

# 為了簡化讀取文件的操作 這種寫法，with語句的寫法
# 既簡單又安全,當with語句執行完成 關閉文件操作自動完成
with open("1.txt", "r") as file:
    file_data = file.read()
    print(file_data) 

