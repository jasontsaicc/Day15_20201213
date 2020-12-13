# 一个类只要实现了__enter__()和__exit__()这个两个方法，通过该类创建的对象我们就称之为上下文管理器。
class File(object):
    def __init__(self, file_name, file_mode):
        # 定义变量保存文件名和打开模式
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        # 上文方法 負責返回操作對象資源，比如:文件對象，數據庫連接對象
        self.file =open(self.file_name, self.file_mode)
        return self.file

    # 當with語句執行完成以後自動執行__ exit_ 方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法，負責釋放對象資源，比如:關閉文件，關閉數據庫連接對象
        print("over")
        self.file.close()

# with 語句結合上下文管理器對象使用
with File("1.txt", "r") as file:
    file_data = file.read()
    print(file_data)
        

