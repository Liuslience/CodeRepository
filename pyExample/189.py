class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        # temp = nums[l - k : l + 1]
        nums[:] = nums[l - k : l + 1] + nums[:l - k]
        nums = [0, 0]

result = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
result.rotate(nums, k)
print(nums)
