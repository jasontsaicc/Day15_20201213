import re
# 代碼	功能
# .	    匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s。	匹配空白，即空格，tab鍵
# \S。	匹配非空白
# \w。	匹配非特殊字元，即a-z、A-Z、0-9、_、漢字
# \W。	匹配特殊字符，即非字母、非数字、非汉字

# 1.匹配任意1个字符（除了\n）
match_obj = re.match("t.o", "t/no")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    # 匹配失敗match_obj是一個None
    print("匹配失敗")


# []匹配[ ]中列举的字符
# []內不用加逗號"," 不然會匹配到
match_obj = re.match("Iron Man[12]", "Iron Man2")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    # 匹配失敗match_obj是一個None
    print("匹配失敗")