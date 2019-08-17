

s = "-91283472332"
n = len(s)
i = 0
now_str = ''
get_num = False
while True and i<n:
    str1 = s[i]
    i += 1
    if  get_num:
        if str1 <= '+' or str1 >= '9':
            break
        else:
            now_str = now_str + str1
    else:
        if str1 <= '+' or str1 >= '9':
            pass
        else:
            now_str = now_str + str1
            get_num = True

num = int(now_str)
