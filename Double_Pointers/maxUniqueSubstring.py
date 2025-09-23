"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


import typing

class Solution:
    def maxUniqueSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                left += 1
                char_set.remove(s[left])
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
            

# Test
'''print(Solution().maxUniqueSubstring("abcabcbb"))
assert Solution().maxUniqueSubstring("abcabcbb") == 3
assert Solution().maxUniqueSubstring("bbbbb") == 1'''
assert Solution().maxUniqueSubstring("pwwkew") == 3

