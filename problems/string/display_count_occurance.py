
def get_count_string(s):
    res = ""
    temp = s[0]
    count = 0
    for i in range(len(s)):
        if temp == s[i]:
            count = count + 1
        else:
            res = res + temp +str(count)
            temp = s[i]
            count = 0
    else:
        res = res + temp + str(count)
    return res


strs ="aabbb"
re = get_count_string(strs)
# print(re)


