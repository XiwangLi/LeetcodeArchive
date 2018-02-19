# # 4: String to Integer (atoi)
# this problem is not hard, but there are some corner cases. 
# 1: with sign or not
# 2: number larger/smaller the sysMAX, sysMIN
# 3 non digital str
def myAtoi(st):
    ls = list(st.strip())
    if len(st) == 0: return 0
    sign = -1 if ls[0] == '-' else 1
    if ls[0] == '-' or ls[0] == '+':
        ls = ls[1 :]
    ans, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ans = ans * 10 + int(ls[i])
        i += 1    
    return min(2147483647, ans*sign) if ans*sign > 0 else max(-2147483648, ans*sign)