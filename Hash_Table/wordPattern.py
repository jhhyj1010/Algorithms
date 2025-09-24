"""
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

示例1:
输入: pattern = "abba", s = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", s = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false

提示:
1 <= pattern.length <= 300
pattern 只包含小写英文字母
1 <= s.length <= 3000
s 只包含小写英文字母和 ' '
s 不包含 任何前导或尾随对空格
s 中每个单词都被 单个空格 分隔
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p2w = {}
        w2p = {}
        
        for p, w in zip(pattern, words):
            if p not in p2w:
                p2w[p] = w
            else:
                if p2w[p] != w:
                    return False
            
            if w not in w2p:
                w2p[w] = p
            else:
                if w2p[w] != p:
                    return False
        
        return True
    
    def wordPattern_simple(self, pattern: str, s: str) -> bool:
        words = [word for word in s.split(' ')]
        p_index = [pattern.index(c) for c in pattern]
        w_index = [words.index(w) for w in words]
        if p_index == w_index:
            return True
        return False


# Test
pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern_simple(pattern, s))