"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
则可以认为该短语是一个 回文串 。字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
示例 1：

输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
示例 2：

输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
示例 3：

输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isalnum()]
        i = 0
        j = len(new_s) - 1
        while i < j:
            if new_s[i] == new_s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


# test
s = "A man, a plan, a canal: Panama"
s1 = "race a car"
sol = Solution()
print(sol.isPalindrome(s))
print(sol.isPalindrome(s1))