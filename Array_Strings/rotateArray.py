"""
给定一个整数数组 nums,将数组中的元素向右轮转 k 个位置,其中 k 是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7],k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: nums = [-1,-100,3,99], k = 2
输出:[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""

import typing
class Solution:
    def rotate(self, nums: typing.List[int], k: int) -> None:
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())
    
    def rotate_new(self, nums: typing.List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


array = [1,2,3,4,5,6,7]
sol = Solution()
sol.rotate_new(array, 3)
print(array)

"""
In rotate_new(nums, k),
reverse(0, n-1):
[1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
reverse(0, k-1):
[7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
reverse(k, n-1):
[5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
"""