class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        num = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[num] = nums[i]
                nums[i] = 0
                num += 1




            



result = Solution()
nums = [0,1,0,3,12]
result.moveZeroes(nums)
print(nums)

# a = list(range(1, len(nums)))
# print(a[::-1])


