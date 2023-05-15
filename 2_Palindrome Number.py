class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        t = s[::-1]
        return s == t
