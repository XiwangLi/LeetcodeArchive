## 1: Implement strStr()  Leetcode 28
# The first question is StrStr. It is the first problem in almost all the books of pactice material
# The brute force way of solve this problem is very easy and the time-complexity is O(m*n). 
# Everybody will say, the brute force O(m*n) method is not good. We want better one. People recommended KMP. 
# I also tried KMP,but it is so hard to follow. So here I will try another algorithem called Robin-Karp. 
# The whole idea is to scan over the string and adding the new one/deleting the first one at the same time

def strstrBF(haystack, needle):
    m, n = len(haystack), len(needle)
    for i in range(m -n + 1):
        if haystack[i: i + n] == needle:
            return i
    return -1

def RobinKarp(haystack, needle):
    base = 26
    # calculate the hash for haystack (the first n-lenght substring) and needle 
    hash_h = reduce(lambda h, c: h * base + ord(c), haystack[: len(needle)], 0)
    hash_n = reduce(lambda h, c: h * base + ord(c), needle, 0)
    power = max(base ** (len(needle) - 1), 0) # in case len(needle) is 0, how many time that ord(c) mutiplied by base
    for i in range(len(needle),  len(haystack)):  #then scan the whole string ahead
        if hash_h == hash_n: 
            return i - len(needle)
        hash_h -= power * ord(haystack[i - len(needle)])        # substract the first chara
        hash_h = hash_h * base + ord(haystack[i])
    if hash_h == hash_n: 
        return len(haystack) - len(needle)    # check the last substring
    return -1

print strstrBF('haystack', 'yst')
print RobinKarp('haystack', 'yst')