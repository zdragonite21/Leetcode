#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import Counter
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        i = 0
        j = 0
        while j < len(s):
            c[s[j]] += 1
            if not all(x < 2 for x in c.values()):
                c[s[i]] -= 1
                j += 1
                i += 1
            else:
                j += 1
        return j - i
            
                
                
# @lc code=end

