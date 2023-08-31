#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
def isPal(s):
    return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(isPal("abcba"))

        for l in range(len(s), 0, - 1):
            for i in range(len(s) - l + 1):
                ss = s[i : i + l] 
                if isPal(ss):
                    return ss

# @lc code=end

