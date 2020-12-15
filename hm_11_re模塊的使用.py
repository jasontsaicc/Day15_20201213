import re
# 根據正則表達式匹配數據
# 1.正則表達式
# 2.要匹配的字符串
match_obj = re.match("hel", "hello python")
# 獲取匹配結果
result = match_obj.group()

print(result)