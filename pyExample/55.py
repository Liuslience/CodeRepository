class Solution:
    def canJump(self, nums):
        result = 0
        CurStep = 0
        NextStep = 0
        for i in range(len(nums)):
            if CurStep <= len(nums) - 1:
                CurStep += max([j + CurStep for j in nums[CurStep + 1 : CurStep + nums[CurStep] + 1]])
            else:
                return True

        if CurStep == len(nums) - 1:
            return True
        else:
            return False
        

result = Solution()
nums = [3,2,1,0,4]
print(result.canJump(nums))

# CurStep = 0
# nums = [2,3,1,1,4]
# print([j + CurStep for j in nums[CurStep + 1 : CurStep + nums[CurStep] + 1]])




