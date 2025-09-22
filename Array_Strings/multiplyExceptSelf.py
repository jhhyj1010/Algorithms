"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""


import typing
class Solution:
    def productExceptSelf(self, nums: typing.List[int]) -> typing.List[int]:
        length = len(nums)
        L, R, results = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1]*nums[i-1]

        R[length-1] = 1
        for j in reversed(range(length - 1)):
            R[j] = R[j+1]*nums[j+1]
        
        for k in range(length):
            results[k] = L[k] * R[k]
        return results


# Test
nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))
