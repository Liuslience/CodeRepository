class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.backtracking(0, candidates, target, 0,  [], result)
        return result
    
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
candidates = [2,3,6,7]
target = 7
print(result.combinationSum(candidates, target))