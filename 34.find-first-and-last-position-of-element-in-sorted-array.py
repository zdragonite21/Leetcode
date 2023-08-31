#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        s, e = 0, 0
        l = -1
        r = n
        print("st")
        while r - l > 1:
            m = (l + r) // 2
            print(f"l {l}, r {r}, m {m}")
            if nums[m] < target:
                l = m
            else:
                r = m
        print(f"l {l}, r {r}, m {m}")
        s = r

        l = -1
        r = n
        print("en")
        while r - l > 1:
            m = (l + r) // 2
            print(f"l {l}, r {r}, m {m}")
            if nums[m] > target:
                r = m
            else:
                l = m
        print(f"l {l}, r {r}, m {m}")
        e = l
        return [s, e] if s <= e else [-1, -1]


# @lc code=end
