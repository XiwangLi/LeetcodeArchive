# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

class Solution(object):
	def validPalindromeI(self, s):
		m, n = 0, len(s) - 1
		while m < n:
			while not s[m].isalnum() and m < n:
				m += 1
			while not s[n].isalnum() and m < n:
				n -= 1
			if s[m].lower() != s[n].lower(): return False
			m += 1
			n -= 1
		return True
    

    def validPalindrome(self, s):
        i = 0
        while i < len(s) / 2 and s[i] == s[-i-1]:
        	i += 1
        s = s[i : len(s)-i]
        if s[1 :] == s[1 :][: : -1] or s[:-1] == s[:-1][: : -1]:
        	return True
        return False




test = Solution()
nums = "abca"
print (test.validPalindrome(nums))

nums1 = "A man, a plan, a canal: Panama"
print (test.validPalindromeI(nums1))