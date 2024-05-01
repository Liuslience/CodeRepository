class Solution:
    def permute(self, nums):
        result = []
        n= len(nums)
        self.backtracking(nums, [], [False] * len(nums), result)
        return result
    def backtracking(self, nums, path, used, result):

        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

            




result = Solution()
num = [1,2,3]
print(result.permute(num))