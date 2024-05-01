class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        l = 1
        length = []
        if len(nums) != 0:
            for i in range(len(nums) - 1):
                if nums[i] + 1 == nums[i + 1]:
                    l += 1
                elif nums[i] == nums[i + 1]:
                    pass
                else:
                    length.append(l)
                    l = 1
        else:
            l = 0
        length.append(l)

        return max(length)

result = Solution()
nums = [1,2,0,1]
print(result.longestConsecutive(nums))