class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        p = list(p)
        for i in range(len(s) - len(p)):
            a = list(s[i : i+len(p)])
            a.sort()
            if a == p:
                result.append(i)
        return result
    
result = Solution()
s = "cbaebabacd"
p = "abc"
print(result.findAnagrams(s, p))