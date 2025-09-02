"""
给你一个数组 nums 和一个值 val,你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。
然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k,要通过此题,您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
"""

class Solution:
    def removeElements(self, nums: list, val: int) -> int:
        count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
        return count


nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElements(nums=nums, val=val))

# Analysis, put the values not equal to val to nums according the original order
# For instance, [0,1,2,2,3,0,4,2] -> [0,1,3,0,4] after the operation.