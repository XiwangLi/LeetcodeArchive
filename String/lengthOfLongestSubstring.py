## 7: Longest Substring Without Repeating Characters
# Given "abcabcbb", the answer is "abc", which the length is 3.
# This type of long substring, sublist, sub... can use two-pointer methods
# use a fast pointer to count each char as save it to a hashtable
# While Val[fast].count > 1, use slow point to remove the val[fast]

def lengthOfLongestSubstring(s):
    slow, fast = 0, 0
    hashmap = {}
    maxlen = 0
    while fast < len(s):
        if s[fast] in hashmap:
            hashmap[s[fast]] = hashmap.get(s[fast], 0) + 1
        else:
            hashmap[s[fast]] = 1
        while  hashmap.get(s[fast], 0)  > 1:
            hashmap[s[slow]]= hashmap.get(s[slow], 0)- 1                   
            slow += 1
        maxlen = max(maxlen, fast - slow + 1)
        fast +=1
    return maxlen

lengthOfLongestSubstring('abcabcbb')