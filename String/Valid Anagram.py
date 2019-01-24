# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        counter = [0] * 26

        for i in range(len(s)):
        	counter[ord(s[i]) - ord('a')] += 1
        	counter[ord(t[i]) - ord('a')] -= 1

        for count in counter:
        	if count != 0:
        		return False
        return True 

test = Solution()
s = "anagram"
t = "nagaram"
print (test.isAnagram(s, t))


