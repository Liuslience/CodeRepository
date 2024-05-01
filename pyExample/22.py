class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        return
    
    def backtracking(self, StartIndex, candidates, target, total, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        if sum(path) > target:
            return

        
        for i in range(StartIndex, len(candidates)):
            path.append(candidates[i])
            self.backtracking(i, candidates, target, total, path, result)
            path.pop()
    
result = Solution()
n = 3
print(result.generateParenthesis(n))