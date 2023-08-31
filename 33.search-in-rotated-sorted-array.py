#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # right = nums[-1]
        # left = nums[0]
        # l = -1
        # r = len(nums)
        # # if len(nums) == 1:
        # #     return 0 if nums[0] == target else -1
        # while r - l > 1:
        #     m = (r + l) // 2
        #     print(l, r, m)
        #     if nums[m] == target:
        #         return m
        #     if left > right:
        #         if target < nums[m]:
        #             if target <= left:
        #                 r = m
        #                 right = nums[r]
        #             else:
        #                 l = m
        #                 left = nums[l]

        #         else:
        #             if target >= right:
        #                 l = m
        #                 left = nums[l]
        #             else:
        #                 r = m
        #                 right = nums[r]
        #     else:
        #         if target < nums[m]:
        #             r = m
        #         else:
        #             l = m
        # # if nums[r] == target:
        # #     return r
        # if nums[l] == target:
        #     return l
        # return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                # left array sorted
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # right array sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


# @lc code=end
