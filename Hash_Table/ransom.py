"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true

提示：
1 <= ransomNote.length, magazine.length <= 105
ransomNote 和 magazine 由小写英文字母组成
"""

import typing
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = 0
        mag = list(magazine)
        for c in list(ransomNote):
            if c in mag:
                cnt += 1
                mag.remove(c)
        if cnt == len(ransomNote):
            return True
        return False
    
    def canConstruct_refined(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        cnt = defaultdict(int)
        for c in magazine:
            cnt[c] += 1
        for i in ransomNote:
            cnt[i] -= 1
        return all(c >= 0 for c in cnt.values())


# Test
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
print(Solution().canConstruct_refined(ransomNote, magazine))