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

# 2.匹配出gmail, hotmail, yahoo
# \.表示對正則表達式裡面的"."進行了轉義.變成了一個普通點 只能匹配.字符
# (gmail|hotmail|yahoo) 表示一個分組，分組從1開始
match_obj = re.match("[a-zA-Z0-9_.]{4,20}@(gmail|hotmail|yahoo)\.com","jasont.saicc@gmail.com")
if match_obj:
    result = match_obj.group(0)
    print(result)
else:
    print("匹配失敗")