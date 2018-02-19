## 2: Reverse Words in a String II
# The key idea of solving this problem is to "reverse the string TWICE"
# Given s = "the sky is blue",
# reverse onceL eht yks si eulb ---> find the space and reverse the word
# reverse twice: blue is sky the --> reverse the whole string

def reverseWords(s):
    s.split()
    idx = 0       
    for i in range (len(s)):
        if s[i] == ' ':
            s[idx : i] = reversed(s[idx : i])
            idx = i + 1
    s[idx :] = reversed(s[idx : ])
    s.reverse()