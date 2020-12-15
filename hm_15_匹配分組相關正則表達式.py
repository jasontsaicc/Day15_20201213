import re
# 代码	功能
# |	    匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

#1. "|" 匹配左右任意一个表達式
fruit_list = ["apple", "benana", "pear", "peach", "orage"]
for value in fruit_list:
    match_obj = re.match("benana|pear",value)
    if match_obj:
        result = match_obj.group()
        print("我愛吃的fruit：" + result)
    else:
        print("我不吃的fruit：" + value)