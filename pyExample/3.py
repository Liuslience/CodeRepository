class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = []
        l = 0
        s = list(s)
        for i in s:
            if i not in a:
                a.append(i)
                if len(a) > l:
                    l = len(a)
            else:
                a = a[a.index(i) : ]

        return l
    
result = Solution()
str = "bbbbb"
print(result.lengthOfLongestSubstring(str))