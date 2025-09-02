"""
给你一个有序数组 nums,请你原地删除重复出现的元素，使得出现次数超过两次的元素只出现两次,
返回删除后数组的新长度。
不要使用额外的数组空间,你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""

from collections import defaultdict


class Solution:
    def removeDuplicatesII(self, nums: list) -> int:
        record = defaultdict(int)
        index = 0
        for n in nums:
            if n not in record or (n in record and record.get(n) < 2):
                record[n] += 1
                nums[index] = n
                index += 1
        return index

    def removeDuplicatesII_refined(self, nums: list) -> int:
        stack_size = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size - 2]:
                nums[stack_size] = nums[i]
                stack_size += 1
        return min(stack_size, len(nums))


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
nums1 = [0, 1, 0, 2, 3, 3, 1]  # NOT the right case, as the nums is an ordered array
sol = Solution()
print(sol.removeDuplicatesII(nums=nums))
print(sol.removeDuplicatesII_refined(nums1))

"""
Original Method: use defaultdict for tracking the occurrence of duplicated elements, index is
used as a counter and index of nums.
Refined Method: use stack for tracking duplicates.
"""
