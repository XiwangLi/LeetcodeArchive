## 8: Longest Substring with At Most Two Distinct Characters
# For example, Given s = “eceba”,
# T is "ece" which its length is 3.

# Different to P7, this problem requires the lenth of the hashmap <= 2
# When the count of one char <= 0, we need remove this char from hashmap

def lengthOfLongestSubstringTwoDistinct(s):
    slow, fast = 0, 0
    hashmap = {}
    maxlen = 0
    while fast < len(s):
        if s[fast] in hashmap:
            hashmap[s[fast]] = hashmap.get(s[fast], 0) + 1
        else:
            hashmap[s[fast]] = 1
        while len(hashmap) > 2:
            hashmap[s[slow]]= hashmap.get(s[slow], 0) - 1                   
            if hashmap.get(s[slow], 0) <= 0:
                del hashmap[s[slow]]
            slow += 1
        maxlen = max(maxlen, fast - slow + 1)
        fast += 1
    return maxlen


lengthOfLongestSubstringTwoDistinct('eceba')
