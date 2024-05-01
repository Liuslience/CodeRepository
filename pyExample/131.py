class Solution:
    def partition(self, s: str):
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, StartIndex, path, result):
        if StartIndex == len(s):
            result.append(path[:])
            return
        
        for i in range(StartIndex + 1, len(s) + 1):
            sub = s[StartIndex : i]
            if self.isPalindrome(sub):
                path.append(sub)
                self.backtracking(s, i, path, result)
                path.pop()

    def isPalindrome(self, s):
        return s == s[::-1]



result = Solution()
s = "aab"
print(result.partition(s))