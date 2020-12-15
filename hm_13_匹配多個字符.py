import re
# 代碼	功能
# *	    匹配前一個字符出現0次或者無限次，即可有可無
# +	    匹配前一個字符出現1次或者無限次，即至少有1次
# ?	    匹配前一個字符出現1次或者0次，即要么有1次，要么沒有
# {m}	匹配前一個字符出現m次
# {m，n} 匹配前一個字符出現從m到n次

# 1."*"匹配前一個字符出現0次或者無限次，即可有可無
# 也可用ta.*wan ,匹配ta234wan or tawan
match_obj = re.match("tai*wan","taiiiiiiiiwan")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失敗")


# 2.+ 匹配前一個字符出現1次或者無限次，即至少有1次
match_obj = re.match("ta.+wan","tawan")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失敗")

#3. ? 匹配前一個字符出現1次或者0次，即要么有1次，要么沒有
match_obj = re.match("https?","http")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失敗")

#4. {m}	匹配前一個字符出現m次
match_obj = re.match("ht{2}p","http")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失敗")