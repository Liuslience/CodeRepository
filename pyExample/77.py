class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        return
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path)
    
result = Solution()
num = [1,2,3]
print(result.permute(num))