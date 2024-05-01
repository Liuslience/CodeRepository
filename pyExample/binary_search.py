class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            
            if nums[middle] < target:
                left = middle
            elif nums[middle] > target:
                right = middle
            else:
                return middle
            
        return -1

result = Solution()
nums = [1,2,5,16,44,49,55,56,77,81,100]
print(result.search(nums, 44))