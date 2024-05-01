class Solution:
    def romanToInt(self, s: str) -> int: 
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)
        for i in range(len(s) - 1):
            if Roman2Int[s[i]] < Roman2Int[s[i+1]]:
                Int = Int - Roman2Int[s[i]]
            else:
                Int = Int + Roman2Int[s[i]]
        return Int + Roman2Int[s[-1]]  


s = "III"
result = Solution()
print(result.romanToInt(s))











