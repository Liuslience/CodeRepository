class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        left = 0
        right = 0
        l = float('inf')

        while right < len(nums):
            if sum(nums[left : right]) < target:
                right += 1
            elif sum(nums[left : right]) > target:
                left += 1
            else:
                l = min(l, len(nums[left : right]))
                right += 1
        
        return l if l != float('inf') else 0
    
result = Solution()
target = 11
nums = [1,2,3,4,5]
print(result.minSubArrayLen(target, nums))