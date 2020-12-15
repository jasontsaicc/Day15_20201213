import re
# 代碼	功能
# ^	    匹配字符串開頭
# $	    匹配字符串結尾

# 1."^" 匹配字符串開頭
# 數字開頭
march_obj = re.match("^\d.*","1abc")
if march_obj:
    result = march_obj.group()
    print(result)
else:
    print("匹配失敗")

# 數字結尾
march_obj = re.match(".*\d$","1abc1")
if march_obj:
    result = march_obj.group()
    print(result)
else:
    print("匹配失敗")

# 開頭數字 結尾數字
march_obj = re.match("^\d.*\d$","1abcsdf7")
if march_obj:
    result = march_obj.group()
    print(result)
else:
     print("匹配失敗")

# [^指定字符] 除了指定字符都匹配
# [^47]$ 除了4.7都批配
march_obj = re.match("^\d.*[^47]$","1abcsdf7")
if march_obj:
    result = march_obj.group()
    print(result)
else:
     print("匹配失敗")