from contextlib import contextmanager

@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        # yield 之前的代碼是上文法方法，負責返回操作對象資源
        yield file
    except Exception as e:
        print(e)

    finally:
        # yield 關鍵後面的代碼可以是下文方法，負責釋放操作對象資源
        file.close()

# 普通語句不能結合with語句使用 ，with語句結合上下文管理器
with my_open("1.txt", "r") as file:
    file_data = file.read()
    print(file_data)
    file.write("test!")